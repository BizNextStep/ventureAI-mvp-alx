import React, { useState } from 'react';
import AddBusinessIdea from './AddBusinessIdea';

const App = () => {
    const [ideas, setIdeas] = useState([]);

    const handleAddIdea = (newIdea) => {
        setIdeas([...ideas, newIdea]);
    };

    return (
        <div>
            <h1>Business Ideas</h1>
            <AddBusinessIdea onAddIdea={handleAddIdea} />
            <ul>
                {ideas.map((idea, index) => (
                    <li key={index}>
                        <h3>{idea.idea}</h3>
                        <p>{idea.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;

