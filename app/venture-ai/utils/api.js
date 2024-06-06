import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
});

export const fetchBusinessIdeas = async () => {
  const response = await api.get('/business_ideas');
  return response.data;
};

export const submitBusinessIdea = async (idea) => {
  const response = await api.post('/business_ideas', idea);
  return response.data;
};

export const fetchUserProfile = async (userId) => {
  const response = await api.get(`/user?id=${userId}`);
  return response.data;
};

