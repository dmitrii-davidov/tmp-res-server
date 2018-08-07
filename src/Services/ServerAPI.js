import api from 'apisauce';


export default class ServerAPI {
  constructor() {
    this._api = api.create({
      baseURL: 'http://localhost:3000/api/',
      timeout: 10000,
    });
  }

  uploadFile({file}) {
    const data = new FormData();
    data.append('file', file);
    return this._api.post('resources/images/', data);
  }
}
