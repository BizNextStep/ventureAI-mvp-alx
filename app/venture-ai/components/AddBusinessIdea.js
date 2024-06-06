import React, { useState } from 'react';
import axios from 'axios';

const AddBusinessIdea = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [industry, setIndustry] = useState('');
  const [investmentPotential, setInvestmentPotential] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const idea = {
      title,
      description,
      industry,
      investmentPotential,
    };
    try {
      await axios.post('/api/business_ideas', idea);
      alert('Business idea submitted successfully!');
    } catch (error) {
      alert('Error submitting business idea. Please try again.');
    }
  };

  return (
    <div>
      <h2>Add Business Idea</h2>
      <form onSubmit={handleSubmit}>
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
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddBusinessIdea;

