import api from 'apisauce';


export default class ServerAPI {
  constructor() {
    this._api = api.create({
      baseURL: '/api/',
      timeout: 10000,
    });
  }

  uploadFile({file}) {
    const data = new FormData();
    data.append('file', file);
    return this._api.post('resources/images/', data);
  }
}
