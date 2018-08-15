import React from 'react';
import {Link} from 'react-router-dom';

import {Container, Form, FormGroup, FormText, Jumbotron, Input, Label} from 'Components/Base';
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
        <Jumbotron className="text-center">
          <h1>Temporary Resource Server</h1>
          <p>It's dangerous to go alone! Use this.</p>
        </Jumbotron>
        <Container>
          <Form>
            <FormGroup>
              <Label>
                Upload a new image
              </Label>
              <Input type="file" onChange={event => this.handleFileHasBeenChanged(event)} />
              <FormText>
                {this.state.imageID &&
                <Link to={`/preview/${this.state.imageID}`}>
                  link
                </Link>
                }
              </FormText>
            </FormGroup>
          </Form>
        </Container>
      </div>
    );
  }
}
