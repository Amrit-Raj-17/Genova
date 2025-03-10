import React from "react";
import { Link } from "react-router-dom";
import "../styles/navbar.css";  // Import CSS

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Helpdesk Support</h1>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/student-portal">Student Portal</Link>
        <Link to="/dashboard">Admin Dashboard</Link>
      </div>
    </nav>
  );
};

export default Navbar;
