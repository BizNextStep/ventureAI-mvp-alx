import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import BusinessIdeaList from './components/BusinessIdeaList';
import AddBusinessIdea from './components/AddBusinessIdea';
import UserProfile from './components/UserProfile';

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={BusinessIdeaList} />
        <Route path="/add-business-idea" component={AddBusinessIdea} />
        <Route path="/user-profile" component={UserProfile} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
