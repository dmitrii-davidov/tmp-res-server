import React from 'react';
import {Redirect} from 'react-router-dom';


// const Preview = ({match}) => <img src={`/api/resources/images/${match.params.id}/`} onError={e => console.error(e)} />;

class Preview extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      loadingError: null,
    };
  }

  handleLoadingError(error) {
    this.setState({loadingError: error});
  }

  render() {
    if (this.state.loadingError) {
      return <Redirect to="" />;
    }
    return (<img
      src={`/api/resources/images/${this.props.match.params.id}/`}
      onError={error => this.handleLoadingError(error)}
      alt="preview"
    />);
  }
}

export default Preview;
