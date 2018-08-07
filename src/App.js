/* @flow */

import React from 'react';
import {BrowserRouter as Router, Route, Redirect, Switch} from 'react-router-dom';

import {Route as Main} from 'Modules/Main';
import {Route as Preview} from 'Modules/Preview';


const App = () => (
  <Router>
    <Switch>
      <Route exact path="/" component={Main} />
      <Route path="/preview" component={Preview} />
      <Redirect to="/" />
    </Switch>
  </Router>
);

export default App;
