import { createContext } from "react";
import { Resume } from "@/types/resume";
import { LoadingState } from "@/types/state";

export interface ResumeContextType {
  parsingState: LoadingState;
  markdown: string;
  resume: Resume | null;
  setParsingState: (state: LoadingState) => void;
  setMarkdown: (markdown: string) => void;
  setResume: (resume: Resume | null) => void;
}

export const ResumeContext = createContext<ResumeContextType | undefined>(
  undefined
);
