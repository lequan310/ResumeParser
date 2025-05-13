import { Resume } from "@/types/resume";
import axiosInstance from "@/services/axiosInstance";

const parseService = {
    parseResume: async (file: File) => {
        const formData = new FormData();
        formData.append("file", file);
        const response = await axiosInstance.post(
            "/api/v1/files/resume",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        const responseObject = response.data["response"];
        const parsedResume: Resume = responseObject["output"];
        const resumeMarkdown = `${responseObject["markdown"]}\n\nAdditional Clarification:\n- Year of Experience: ${parsedResume["yoe"]["year"]} years ${parsedResume["yoe"]["month"]} months`;

        return {
            markdown: resumeMarkdown,
            object: parsedResume,
        };
    },
};

export default parseService;
