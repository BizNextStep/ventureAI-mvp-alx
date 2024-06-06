import React, { useState } from 'react';

const AddBusinessIdea = ({ onAddIdea }) => {
	    const [idea, setIdea] = useState('');
	    const [description, setDescription] = useState('');

	    const handleSubmit = (e) => {
		            e.preventDefault();
		            if (idea && description) {
				                onAddIdea({ idea, description });
				                setIdea('');
				                setDescription('');
				            }
		        };

	    return (
		            <form onSubmit={handleSubmit}>
		                <div>
		                    <label>
		                        Business Idea:
		                        <input
		                            type="text"
		                            value={idea}
		                            onChange={(e) => setIdea(e.target.value)}
		                            required
		                        />
		                    </label>
		                </div>
		                <div>
		                    <label>
		                        Description:
		                        <textarea
		                            value={description}
		                            onChange={(e) => setDescription(e.target.value)}
		                            required
		                        />
		                    </label>
		                </div>
		                <button type="submit">Add Idea</button>
		            </form>
		        );
};

export default AddBusinessIdea;

