import { useContext } from "react";
import { AnalysisContext } from "@/context/AnalysisContext";

const useAnalysisContext = () => {
    const context = useContext(AnalysisContext);

    if (context === undefined) {
        throw new Error(
            "useAnalysisContext must be used within a AnalysisProvider"
        );
    }

    return context;
};

export default useAnalysisContext;
