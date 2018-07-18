import api from 'apisauce';


export default class ServerAPI {
  constructor() {
    this._api = api.create({
      baseURL: 'http://localhost:3000/',
      timeout: 10000,
    });
  }

  uploadFile() {
    return this._api.get('manifest.json');
  }
}
