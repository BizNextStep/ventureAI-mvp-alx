import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to Idea-2-Venture</h1>
      <p>
        This platform is designed to help small to medium-sized businesses prepare for venture capital investment by providing a centralized platform for sharing, collaborating, and developing business ideas.
      </p>
      <p>
        <Link to="/ideas">Browse Business Ideas</Link>
      </p>
      <p>
        <Link to="/user-profile">View Your Profile</Link>
      </p>
    </div>
  );
};

export default HomePage;

