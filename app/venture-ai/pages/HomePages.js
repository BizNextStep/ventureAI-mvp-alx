# Import necessary libraries
import React from 'react';
import { Link } from 'react-router-dom';

# Define the HomePage component
const HomePage = () => {
  // Return JSX for the home page
  return (
    // Create a div to hold the home page content
    <div>
      <h1>Welcome to Idea-2-Venture</h1>
      <p>
        // Provide a brief description of the platform
        This platform is designed to help small to medium-sized businesses prepare for venture capital investment by providing a centralized platform for sharing, collaborating, and developing business ideas.
      </p>
      <p>
        // Provide a link to browse business ideas
        <Link to="/ideas">Browse Business Ideas</Link>
      </p>
      <p>
        // Provide a link to view the user profile
        <Link to="/user-profile">View Your Profile</Link>
      </p>
    </div>
  );
};

// Export the HomePage component
export default HomePage;
