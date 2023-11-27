import React, { useState, useEffect } from 'react';
import UrlInput from './components/UrlInput';
import ChatInterface from './components/ChatInterface';

function App() {
  const [showChat, setShowChat] = useState(false); // Add state to control UI transition

  const handleUrlSubmitted = () => {
    setShowChat(true); // Transition to the ChatInterface
  };

  useEffect(() => {
    // This effect will run when the component is unmounted (page refresh or navigating to a new page)
    return () => {
      fetch('http://localhost:5000/delete-index', {
        method: 'POST',
      })
        .then((response) => {
          if (!response.ok) {
            console.error('Error deleting index:', response.statusText);
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    };
  }, []);

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