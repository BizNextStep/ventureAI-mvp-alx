import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserProfilePage = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const response = await axios.get('/api/user', {
          params: {
            id: localStorage.getItem('userId'),
          },
        });
        setUser(response.data);
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    };
    fetchUserProfile();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>User Profile</h1>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      <h2>Submitted Business Ideas</h2>
      <ul>
        {user.business_ideas.map((idea) => (
          <li key={idea.id}>
            <h3>{idea.title}</h3>
            <p>{idea.description}</p>
            <p>Industry: {idea.industry}</p>
            <p>Investment Potential: {idea.investment_potential}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserProfilePage;

