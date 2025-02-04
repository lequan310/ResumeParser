import { useContext } from "react";
import { ResumeContext, ResumeContextType } from "@/context/ResumeContext";

const useResumeContext = (): ResumeContextType => {
    const context = useContext(ResumeContext);

    if (context === undefined) {
        throw new Error(
            "useResumeContext must be used within a ResumeProvider"
        );
    }

    return context;
};

export default useResumeContext;
