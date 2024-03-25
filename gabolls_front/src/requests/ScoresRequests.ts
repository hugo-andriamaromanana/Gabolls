import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL as string;

export const getScores = async () => {
    const response = await axios(`${API_URL}/scores`);
    return response.data;
};

export const addScore = async () => {
    const response = await axios(`${API_URL}/scores`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        data: {}
    });
    return response.data;
};

export const getScore = async (id: string) => {
    const response = await axios(`${API_URL}/scores/${id}`);
    return response.data;
};

export const updateScore = async () => {
    const response = await axios(`${API_URL}/scores/ID`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        data: {}
    });
    return response.data;
};
