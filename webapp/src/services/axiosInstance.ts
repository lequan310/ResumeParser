import axios from "axios";

const axiosInstance = axios.create({
    baseURL: import.meta.env.CORE_API_URL || "http://localhost:3000",
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
    },
});

export default axiosInstance;