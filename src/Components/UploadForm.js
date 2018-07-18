import React from 'react';

import {serverAPI} from 'Services';


export default class UploadForm extends React.Component {
  handleUploadFile(event) {
    return serverAPI();
  }

  render() {
    return (
      <input type="file" onChange={() => this.handleUploadFile} />
    );
  }
}
