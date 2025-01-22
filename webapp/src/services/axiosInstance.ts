import axios from "axios";

const axiosInstance = axios.create({
    baseURL: import.meta.env.CORE_API_URL || "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
    },
});

axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("token");
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axiosInstance.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        console.log(error);
        if (error.response) {
            console.log(error.response.data);
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;
