import { createContext } from "react";

export type PDFFile = File | null;

export interface PDFContextType {
  currentPdf: PDFFile;
  setCurrentPdf: (file: PDFFile) => void;
}

export const PDFContext = createContext<PDFContextType | undefined>(undefined);
