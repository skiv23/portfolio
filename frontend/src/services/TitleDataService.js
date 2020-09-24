import http from '../../http-common'

const baseURL = '/contact/titles/'

class TitleDataService {
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

  filterByType(type) {
    return http.get(`${baseURL}?type=${type}`);
  }
}

export default new TitleDataService();
