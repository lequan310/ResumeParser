import { CircleCheck } from "lucide-react";
import FileUpload from "@/components/FileUpload";
import { useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import MainLayout from "@/layouts/MainLayout";
import parseService from "@/services/parseService";
import { LoadingState } from "@/context/ResumeContext";
import {
  useChatContext,
  useNavContext,
  usePDFContext,
  useResumeContext,
} from "@/hooks";

const PARSE_PATH = "/parse";

const Upload = () => {
  const navigate = useNavigate();
  const pdfContext = usePDFContext();
  const navContext = useNavContext();
  const chatContext = useChatContext();
  const resumeContext = useResumeContext();

  const handleFileSelect = useCallback(
    (file: File) => {
      if (file.type !== "application/pdf") {
        toast.error("Only PDF files are supported");
        return;
      }

      pdfContext.setCurrentPdf(file);
      chatContext.resetChat();
      navContext.setActiveTab("parse");
      resumeContext.setResume(null);
      resumeContext.setMarkdown("");
      resumeContext.setLoadingState("loading");

      parseService
        .parseResume(file)
        .then(({ markdown, object }) => {
          resumeContext.setLoadingState("success" as LoadingState);
          resumeContext.setMarkdown(markdown);
          resumeContext.setResume(object);
          toast.success(file.name + " parsed successfully.");
        })
        .catch((error) => {
          resumeContext.setLoadingState("error" as LoadingState);
          resumeContext.setMarkdown("");
          resumeContext.setResume(null);
          toast.error(error.response.data["detail"]);
        });
    },
    [pdfContext, chatContext, navContext, resumeContext]
  );

  useEffect(() => {
    if (pdfContext.currentPdf && navContext.activeTab === "parse") {
      navigate(PARSE_PATH);
    }
  }, [pdfContext, navContext, navigate]);

  return (
    <MainLayout>
      <h1 className="text-3xl font-bold text-center">Resume Upload</h1>
      <FileUpload onFileSelect={handleFileSelect} />
      <div className="flex gap-x-8 font-normal">
        <p className="flex-grow max-w-[50%]">
          Resume Parser is a tool that converts your resume from PDF or images
          to structured output. Come with free AI-powered resume analysis.
        </p>
        <ul className="flex flex-col space-y-2.5 ml-auto">
          <li className="flex items-center gap-x-2">
            <CircleCheck className="w-4 h-4 text-green-500" />
            Accurately convert resume to structured output.
          </li>
          <li className="flex items-center gap-x-2">
            <CircleCheck className="w-4 h-4 text-green-500" />
            Free, support PDF and images.
          </li>
          <li className="flex items-center gap-x-2">
            <CircleCheck className="w-4 h-4 text-green-500" />
            AI-powered analysis and recommendation.
          </li>
        </ul>
      </div>
    </MainLayout>
  );
};

export default Upload;
