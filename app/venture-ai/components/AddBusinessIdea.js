# Import necessary libraries
import React, { useState } from 'react';
import axios from 'axios';

# Define the AddBusinessIdea component
const AddBusinessIdea = () => {
  // Initialize state variables for title, description, industry, and investment potential
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [industry, setIndustry] = useState('');
  const [investmentPotential, setInvestmentPotential] = useState('');

  // Define the handleSubmit function to handle form submission
  const handleSubmit = async (event) => {
    // Prevent default form submission behavior
    event.preventDefault();

    // Create an object to hold the form data
    const idea = {
      title,
      description,
      industry,
      investmentPotential,
    };

    // Attempt to post the form data to the server
    try {
      // Use Axios to send a POST request to the '/api/business_ideas' endpoint
      await axios.post('/api/business_ideas', idea);

      // Display an alert message if the submission is successful
      alert('Business idea submitted successfully!');
    } catch (error) {
      // Display an alert message if there is an error
      alert('Error submitting business idea. Please try again.');
    }
  };

  // Return the JSX for the form
  return (
    // Create a div to hold the form
    <div>
      <h2>Add Business Idea</h2>
      <form onSubmit={handleSubmit}>
        // Create form fields for title, description, industry, and investment potential
        <label>
          Title:
          <input type="text" value={title} onChange={(event) => setTitle(event.target.value)} />
        </label>
        <br />
        <label>
          Description:
          <textarea value={description} onChange={(event) => setDescription(event.target.value)} />
        </label>
        <br />
        <label>
          Industry:
          <input type="text" value={industry} onChange={(event) => setIndustry(event.target.value)} />
        </label>
        <br />
        <label>
          Investment Potential:
          <input type="text" value={investmentPotential} onChange={(event) => setInvestmentPotential(event.target.value)} />
        </label>
        <br />
        // Create a submit button
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

// Export the AddBusinessIdea component
export default AddBusinessIdea;
