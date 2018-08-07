import React from 'react';
import {Route, Switch} from 'react-router-dom';

import Main from './Containers/Main';


const MainRoute = () => (
  <Switch>
    <Route exact path="/" component={Main} />
  </Switch>
);

export default MainRoute;
