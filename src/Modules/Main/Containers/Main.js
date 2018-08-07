import React from 'react';
import {Link} from 'react-router-dom';

import {serverAPI} from 'Services';


export default class Main extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: false,
      imageID: null,
    };
  }

  handleFileHasBeenChanged(event) {
    this.setState({
      isLoading: true,
    });
    return serverAPI.uploadFile({
      file: event.target.files[0],
    }).then((res) => {
      this.setState({
        isLoading: false,
        imageID: res.data.hashedID,
      });
    });
  }

  render() {
    if (this.state.isLoading) {
      return <p>Image is loading!</p>;
    }
    return (
      <div>
        <div>
          <input type="file" onChange={event => this.handleFileHasBeenChanged(event)} />
        </div>
        {this.state.imageID &&
          <Link to={`/preview/${this.state.imageID}`}>
            <div>link</div>
          </Link>
        }
      </div>
    );
  }
}
