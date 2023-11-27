import React from 'react';
import ReactMarkdown from 'react-markdown';

function ChatMessage({ message }) {
  
  // Only parse markdown for bot messages
  const content = message.isBot ? (
    <ReactMarkdown children={message.text} />
  ) : (
    message.text
  );

  return (
    <div className={`chat-message ${message.isBot ? 'bot-message' : 'user-message'}`}>
      {content}
    </div>
  );
}

export default ChatMessage;