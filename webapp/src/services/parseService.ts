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
        const parsedResume: Resume = responseObject["output"];
        const resumeMarkdown = responseObject["markdown"];

        return {
            markdown: resumeMarkdown,
            object: parsedResume,
        };
    },
};

export default parseService;
