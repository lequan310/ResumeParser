import { createContext } from "react";
import { Analysis } from "@/types/analysis";
import { LoadingState } from "@/types/state";

export interface AnalysisContextType {
  job_desc: string;
  analysisState: LoadingState;
  analysis: Analysis | null;
  setJobDesc: (job_desc: string) => void;
  setAnalysisState: (state: LoadingState) => void;
  setAnalysis: (analysis: Analysis | null) => void;
}

export const AnalysisContext = createContext<AnalysisContextType | undefined>(
  undefined
);
