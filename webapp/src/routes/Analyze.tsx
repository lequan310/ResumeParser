import { useState, useCallback } from "react";
import { toast } from "react-toastify";
import SplitLayout from "@/layouts/SplitLayout";
import SpinLoader from "@/components/SpinLoader";
import ResumeForm from "@/components/resume-form/ResumeForm";
import AnalysisForm from "@/components/analysis-form/AnalysisForm";
import { useResumeContext, useAnalysisContext } from "@/hooks";
import { LoadingState } from "@/types/state";
import analysisService from "@/services/analysisService";

const Analyze = () => {
  const [jobDescription, setJobDescription] = useState<string>("");
  const resumeContext = useResumeContext();
  const analysisContext = useAnalysisContext();

  const analyzeResume = useCallback(() => {
    const resume_markdown = resumeContext.markdown.trim();
    const job_description = jobDescription.trim();

    if (!resume_markdown) {
      toast.error("Please upload a resume and wait for parsing to be done.");
      return;
    }

    if (!job_description) {
      toast.error("Please enter a job description to analyze the resume.");
      return;
    }

    if (analysisContext.analysisState === ("loading" as LoadingState)) {
      toast.info("Analysis is already in progress. Please wait...");
      return;
    }

    analysisContext.setAnalysisState("loading" as LoadingState);
    analysisContext.setAnalysis(null);

    // Call the analysis service
    analysisService
      .analyzeResume(resumeContext.markdown, jobDescription)
      .then((response) => {
        analysisContext.setAnalysis(response);
        analysisContext.setAnalysisState("success" as LoadingState);
        toast.success("Resume analyzed successfully.");
      })
      .catch((error) => {
        analysisContext.setAnalysis(null);
        analysisContext.setAnalysisState("error" as LoadingState);
        toast.error(error.response.data["detail"]);
      });
  }, [analysisContext, resumeContext, jobDescription]);

  return (
    <SplitLayout
      sections={[
        resumeContext.parsingState === ("loading" as LoadingState) ? (
          <div className="flex flex-col items-center justify-center w-full h-full gap-4">
            <SpinLoader size={100} />
            <p className="text-xl animate-pulse">Parsing Resume...</p>
          </div>
        ) : (
          <ResumeForm />
        ),
        <div className="flex flex-col w-full h-full p-4">
          <h2 className="text-xl font-semibold mb-4">Job Description</h2>
          <textarea
            className="h-full p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600 resize-none"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />
        </div>,
        analysisContext.analysisState === ("loading" as LoadingState) ? (
          <div className="flex flex-col items-center justify-center w-full h-full gap-4">
            <SpinLoader size={100} />
            <p className="text-xl animate-pulse">Analyzing Resume...</p>
          </div>
        ) : (
          <AnalysisForm analyzeOnClick={analyzeResume} />
        ),
      ]}
    />
  );
};

export default Analyze;
