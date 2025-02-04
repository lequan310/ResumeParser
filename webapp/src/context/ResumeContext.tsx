import { createContext } from "react";
import { Resume } from "@/types/resume";

export type LoadingState = "loading" | "error" | "success";

export interface ResumeContextType {
  loadingState: LoadingState;
  markdown: string;
  resume: Resume | null;
  setLoadingState: (state: LoadingState) => void;
  setMarkdown: (markdown: string) => void;
  setResume: (resume: Resume | null) => void;
}

export const ResumeContext = createContext<ResumeContextType | undefined>(
  undefined
);
