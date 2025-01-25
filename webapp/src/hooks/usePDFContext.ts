import { useContext } from "react";
import { PDFContext } from "@/context/PDFContext"; // Assuming PDFContext is in the same directory

/**
 * Custom hook to consume the PDFContext.
 * Provides the current PDF file and a function to set it.
 * Throws an error if used outside of a PDFProvider.
 */
const usePDFContext = () => {
    const context = useContext(PDFContext);

    if (context === undefined) {
        throw new Error("usePDFContext must be used within a PDFProvider");
    }

    return context;
};

export default usePDFContext;
