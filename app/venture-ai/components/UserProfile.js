# Import necessary libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

# Define the UserProfile component
const UserProfile = () => {
  // Initialize state variable for user data
  const [user, setUser] = useState(null);

  // Use the useEffect hook to fetch user profile data on component mount
  useEffect(() => {
    // Define an asynchronous function to fetch user profile data
    const fetchUserProfile = async () => {
      // Attempt to fetch user profile data from the server
      try {
        // Use Axios to send a GET request to the '/api/user' endpoint
        const response = await axios.get('/api/user', {
          // Pass the user ID stored in local storage as a query parameter
          params: {
            id: localStorage.getItem('userId'),
          },
        });

        // Update the user state with the fetched data
        setUser(response.data);
      } catch (error) {
        // Log an error message if there is an error fetching user profile data
        console.error('Error fetching user profile:', error);
      }
    };

    // Call the fetchUserProfile function to initiate the fetch
    fetchUserProfile();
  }, []);

  // Check if the user data is available
  if (!user) {
    // Return a loading message if the user data is not available
    return <div>Loading...</div>;
  }

  // Return the JSX for the user profile
  return (
    // Create a div to hold the user profile information
    <div>
      <h2>User Profile</h2>
      // Display the user's username and email
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      <h3>Submitted Business Ideas</h3>
      // Map over the user's business ideas and render each idea as a list item
      <ul>
        {user.business_ideas.map((idea) => (
          <li key={idea.id}>
            <h4>{idea.title}</h4>
            <p>{idea.description}</p>
            <p>Industry: {idea.industry}</p>
            <p>Investment Potential: {idea.investment_potential}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Export the UserProfile component
export default UserProfile;
