import http from '../../http-common'

const baseURL = '/about/timelines/'

class TimelineDataService {
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

export default new TimelineDataService();
