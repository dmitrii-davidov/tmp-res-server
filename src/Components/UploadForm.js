import React from 'react';

import {serverAPI} from 'Services';


export default class UploadForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      imageURL: null,
    };
  }

  handleUploadFile(event) {
    return serverAPI.uploadFile({
      file: event.target.files[0],
    }).then((res) => {
      this.setState({
        imageURL: `http://localhost:3000/api/resources/${res.data.hashedID}/`,
      });
    });
  }

  render() {
    return (
      <div>
        {this.state.imageURL &&
          <img width={320} src={this.state.imageURL} alt="42" />
        }
        <input type="file" onChange={event => this.handleUploadFile(event)} />
      </div>
    );
  }
}
