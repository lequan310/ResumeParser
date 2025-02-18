import { createContext } from "react";
import { Analysis } from "@/types/analysis";
import { LoadingState } from "@/types/state";

export interface AnalysisContextType {
  analysisState: LoadingState;
  analysis: Analysis | null;
  setAnalysisState: (state: LoadingState) => void;
  setAnalysis: (analysis: Analysis | null) => void;
}

export const AnalysisContext = createContext<AnalysisContextType | undefined>(
  undefined
);
