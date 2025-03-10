import React, { useState } from "react";
import "../styles/chatbot.css";  // Import CSS

const Chatbot = () => {
  const [messages, setMessages] = useState(["Hi! How can I assist you today?"]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages([...messages, input]);
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="chatbot">
      <h3>AI Chatbot</h3>
      <div className="chatbox">
        {messages.map((msg, idx) => (
          <p key={idx}>{msg}</p>
        ))}
      </div>
      <input 
        type="text" 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        onKeyDown={handleKeyDown}  // Listen for Enter key
        placeholder="Type your query..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default Chatbot;
