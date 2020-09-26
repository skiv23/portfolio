import http from '../../http-common'

const baseURL = '/about/what-i-do-entries/'

class WhatIDoDataService {
  getAll() {
    return http.get(baseURL);
  }

  get(id) {
    return http.get(`${baseURL}${id}`);
  }

  create(data) {
    return http.post(baseURL, data);
  }

  update(id, data) {
    return http.put(`${baseURL}${id}`, data);
  }

}

export default new WhatIDoDataService();
