import http from '../../http-common'

const aboutBaseURL = '/about/about-entries/'
const aboutInfoBaseURL = '/about/about-info-entries/'

class AboutDataService {

  get() {
    return http.get(`${aboutBaseURL}`);
  }

  create(data) {
    return http.post(aboutBaseURL, data);
  }

  update(id, data) {
    return http.put(`${aboutBaseURL}${id}`, data);
  }

  createInfoEntry(data) {
    return http.post(aboutInfoBaseURL, data);
  }

  updateInfoEntry(id, data) {
    return http.put(`${aboutInfoBaseURL}${id}`, data);
  }

  deleteInfoEntry(id) {
    return http.delete(`${aboutInfoBaseURL}${id}`)
  }
}

export default new AboutDataService();
