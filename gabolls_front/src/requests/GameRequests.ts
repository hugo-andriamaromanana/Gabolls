import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL as string;

export const getGames = async () => {
    const response = await axios.get(`${API_URL}/games`);
    return response.data;
};

export const createGame = async () => {
    const response = await axios(`${API_URL}/alarms`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        data: {}
    });
    return response.data;
};

export const getGame = async (id: string) => {
    const response = await axios.get(`${API_URL}/games/${id}`);
    return response.data;
};

export const updateGame = async () => {
    const response = await axios(`${API_URL}/games/ID`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        data: {}
    });
    return response.data;
};

export const deleteGame = async (id: string) => {
    const response = await axios.delete(`${API_URL}/games/${id}`);
    return response.data;
};
