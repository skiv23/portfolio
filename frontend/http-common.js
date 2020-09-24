import axios from "axios";

let baseURL = "api/v1/";

const apiHost = process.env.VUE_APP_API_HOST || "http://localhost:8000/";
if (apiHost) {
  baseURL = `${apiHost}${baseURL}`;
}

export default axios.create({
  baseURL: baseURL,
  headers: {
    "Content-type": "application/json"
  }
});
