import React from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import StudentPortal from "./pages/StudentPortal";
import Dashboard from "./pages/Dashboard";
import Chatbot from "./components/Chatbot";
import "./styles/global.css"; 

const App = () => {
  return (
    <div className="app-container">
      <Navbar />
      <div className="page-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/student-portal" element={<StudentPortal />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
      <Chatbot />
    </div>
  );
};

export default App;