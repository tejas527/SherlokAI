import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

export const sendMessage = async (message) => {
  const res = await axios.post(`${BASE_URL}/chat`, { message });
  return res.data.response;
};

export const uploadCase = async (caseText) => {
  const res = await axios.post(`${BASE_URL}/start_case`, { case: caseText });
  return res.data.status;
};
