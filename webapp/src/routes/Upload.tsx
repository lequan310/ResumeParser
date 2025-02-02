import { CircleCheck } from "lucide-react";
import FileUpload from "@/components/FileUpload";
import { useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import usePDFContext from "@/hooks/usePDFContext";
import useNavContext from "@/hooks/useNavContext";
import useChatContext from "@/hooks/useChatContext";
import MainLayout from "@/layouts/MainLayout";

const ANALYZE_PATH = "/analyze";

const Upload = () => {
  const navigate = useNavigate();
  const pdfContext = usePDFContext();
  const navContext = useNavContext();
  const chatContext = useChatContext();

  const handleFileSelect = useCallback(
    (file: File) => {
      if (file.type !== "application/pdf") {
        toast.error("Only PDF files are supported");
        return;
      }
      pdfContext.setCurrentPdf(file);
      chatContext.resetChat();
      navContext.setActiveTab("analyze");
    },
    [pdfContext, chatContext, navContext]
  );

  useEffect(() => {
    if (pdfContext.currentPdf && navContext.activeTab === "analyze") {
      navigate(ANALYZE_PATH);
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
