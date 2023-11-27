// src/components/ChatInterface.js
import React, { useState, useEffect, useRef } from 'react';
import ChatMessage from './ChatMessage';

function ChatInterface() {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const handleSendMessage = async (event) => {
    event.preventDefault();
    if (!inputText.trim()) return; // Prevent sending empty messages
    const userMessage = { text: inputText, isBot: false };
    const body = {
      chatHistory: [...messages, userMessage],
      question: inputText,
    }    
    setMessages([...messages, userMessage]);
    setInputText('');

    const response = await fetch('http://localhost:5000/handle-query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const data = await response.json();
    const botMessage = { text: data.answer, isBot: true };
    setMessages(currentMessages => [...currentMessages, botMessage]);
  };

  return (
    <div className="chat-container">
      <header className="chat-header">URL Question & Answer</header>
      <div className="chat-messages">
        {messages.map((message, index) => (
          <ChatMessage key={index} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form className="chat-input" onSubmit={handleSendMessage}>
        <input
          type="text"
          placeholder="Type a question and press enter ..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />

      </form>
    </div>
  );
}

export default ChatInterface;