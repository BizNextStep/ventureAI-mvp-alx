import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BusinessIdeaList = () => {
  const [businessIdeas, setBusinessIdeas] = useState([]);

  useEffect(() => {
    const fetchBusinessIdeas = async () => {
      try {
        const response = await axios.get('/api/business_ideas');
        setBusinessIdeas(response.data);
      } catch (error) {
        console.error('Error fetching business ideas:', error);
      }
    };
    fetchBusinessIdeas();
  }, []);

  return (
    <div>
      <h2>Business Ideas</h2>
      <ul>
        {businessIdeas.map((idea) => (
          <li key={idea.id}>
            <h3>{idea.title}</h3>
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

export default BusinessIdeaList;

