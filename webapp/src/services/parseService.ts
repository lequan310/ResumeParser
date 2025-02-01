import { Resume } from "@/types/resume";
import axiosInstance from "@/services/axiosInstance";

const parseService = {
    parseResume: async (file: File) => {
        const formData = new FormData();
        formData.append("file", file);
        const response = await axiosInstance.post("/files/resume", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
        const responseObject = response.data["response"];
        const parsedResume: Resume = JSON.parse(responseObject);
        return parsedResume;
    },
};

export default parseService;
