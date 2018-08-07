import React from 'react';
import {Route, Switch} from 'react-router-dom';

import Preview from './Containers/Preview';


const PreviewRoute = () => (
  <Switch>
    <Route exact path="/preview/:id" component={Preview} />
  </Switch>
);

export default PreviewRoute;
