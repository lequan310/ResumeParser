import axiosInstance from "@/services/axiosInstance";
import { Analysis } from "@/types/analysis";

const analysisService = {
    analyzeResume: async (resume: string, job_desc: string) => {
        const requestBody = {
            resume: resume,
            job_desc: job_desc,
        };

        const response = await axiosInstance.post("/analysis", requestBody);
        const responseObject: Analysis = response.data["response"];
        return responseObject;
    },
};

export default analysisService;
