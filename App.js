# Import necessary libraries
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import BusinessIdeaList from './components/BusinessIdeaList';
import AddBusinessIdea from './components/AddBusinessIdea';
import UserProfile from './components/UserProfile';

# Define the App component
const App = () => {
  // Return JSX for the application
  return (
    // Wrap the application with the BrowserRouter component
    <BrowserRouter>
      // Use the Switch component to handle routing
      <Switch>
        // Define the route for the home page (business idea list)
        <Route path="/" exact component={BusinessIdeaList} />
        
        // Define the route for adding a new business idea
        <Route path="/add-business-idea" component={AddBusinessIdea} />
        
        // Define the route for the user profile page
        <Route path="/user-profile" component={UserProfile} />
      </Switch>
    </BrowserRouter>
  );
};

// Export the App component
export default App;
