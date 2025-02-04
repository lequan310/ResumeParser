import { Resume } from "@/types/resume";
import { LoadingState } from "@/context/ResumeContext";
import axiosInstance from "@/services/axiosInstance";
import { AxiosError } from "axios";

const parseService = {
    parseResume: async (file: File) => {
        try {
            const formData = new FormData();
            formData.append("file", file);
            const response = await axiosInstance.post(
                "/files/resume",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            const responseObject = response.data["response"];
            const parsedResume: Resume = responseObject["output"];
            const resumeMarkdown = responseObject["markdown"];

            return {
                loadingState: "success" as LoadingState,
                markdown: resumeMarkdown,
                object: parsedResume,
            };
        } catch (error) {
            if (
                error instanceof AxiosError &&
                error.response &&
                error.response.data
            ) {
                return {
                    loadingState: "error" as LoadingState,
                    markdown: error.response.data["detail"],
                    object: null,
                };
            }

            return {
                loadingState: "error" as LoadingState,
                markdown: "Unknown error occurred.",
                object: null,
            };
        }
    },
};

export default parseService;
