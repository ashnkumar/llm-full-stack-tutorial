// src/App.js
import React, { useState, useEffect } from 'react';
import UrlInput from './components/UrlInput';
import ChatInterface from './components/ChatInterface';

function App() {
  const [showChat, setShowChat] = useState(true); // Add state to control UI transition

  const handleUrlSubmitted = () => {
    // Callback function to be called when URL is submitted
    setShowChat(true); // Transition to the ChatInterface
  };

  // useEffect(() => {
  //   // This effect will run when the component is unmounted (page refresh or navigating to a new page)
  //   return () => {
  //     // Add code here to call the 'localhost:5000/delete-index' endpoint
  //     // You can use the fetch API or any other method to make this HTTP request
  //     fetch('http://localhost:5000/delete-index', {
  //       method: 'POST', // Or the appropriate HTTP method for your endpoint
  //     })
  //       .then((response) => {
  //         if (!response.ok) {
  //           console.error('Error deleting index:', response.statusText);
  //         }
  //       })
  //       .catch((error) => {
  //         console.error('Error:', error);
  //       });
  //   };
  // }, []); // The empty dependency array ensures this effect only runs once on component unmount

  return (
    <div className="App">
      {!showChat ? (
        <UrlInput onSubmit={handleUrlSubmitted} />
      ) : (
        <ChatInterface />
      )}
    </div>
  );
}

export default App;