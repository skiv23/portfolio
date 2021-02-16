import http from '../../http-common'

const baseURL = '/contact/contacts/'

class ContactDataService {
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

  filterByComponent(component) {
    return http.get(`${baseURL}?component=${component}`);
  }

  createContactMe(data) {
    return http.post(baseURL + 'me/', data);
  }
}

export default new ContactDataService();
