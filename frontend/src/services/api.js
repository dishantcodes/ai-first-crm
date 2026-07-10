import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-first-crm-api.onrender.com",
});

export default api;
