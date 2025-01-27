import { useContext } from "react";
import { PDFContext } from "@/context/PDFContext"; // Assuming PDFContext is in the same directory

const usePDFContext = () => {
    const context = useContext(PDFContext);

    if (context === undefined) {
        throw new Error("usePDFContext must be used within a PDFProvider");
    }

    return context;
};

export default usePDFContext;
