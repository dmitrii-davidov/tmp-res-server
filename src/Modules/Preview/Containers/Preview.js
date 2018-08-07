import React from 'react';


const Preview = ({match}) => <img src={`/api/resources/images/${match.params.id}/`} />;

export default Preview;
