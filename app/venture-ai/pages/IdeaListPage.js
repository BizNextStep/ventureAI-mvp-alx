# Import necessary libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

# Define the IdeaListPage component
const IdeaListPage = () => {
  // Initialize state variable for business ideas
  const [businessIdeas, setBusinessIdeas] = useState([]);

  // Use the useEffect hook to fetch business ideas on component mount
  useEffect(() => {
    // Define an asynchronous function to fetch business ideas
    const fetchBusinessIdeas = async () => {
      // Attempt to fetch business ideas from the server
      try {
        // Use Axios to send a GET request to the '/api/business_ideas' endpoint
        const response = await axios.get('/api/business_ideas');

        // Update the businessIdeas state with the fetched data
        setBusinessIdeas(response.data);
      } catch (error) {
        // Log an error message if there is an error fetching business ideas
        console.error('Error fetching business ideas:', error);
      }
    };

    // Call the fetchBusinessIdeas function to initiate the fetch
    fetchBusinessIdeas();
  }, []);

  // Return JSX for the idea list page
  return (
    // Create a div to hold the idea list
    <div>
      <h1>Business Ideas</h1>
      // Map over the businessIdeas array and render each idea as a list item
      <ul>
        {businessIdeas.map((idea) => (
          <li key={idea.id}>
            <h2>{idea.title}</h2>
            <p>{idea.description}</p>
            <p>Industry: {idea.industry}</p>
            <p>Investment Potential: {idea.investment_potential}</p>
            <p>Submitted By: {idea.submitted_by}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

# Export the IdeaListPage component
export default IdeaListPage;
