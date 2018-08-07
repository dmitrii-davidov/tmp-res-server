/* @flow */

import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';


const container = document.getElementById('root');
if (!container) {
  throw Error('Container should be not null!');
}
ReactDOM.render(<App />, container);
registerServiceWorker();
