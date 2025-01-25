import { CircleCheck } from "lucide-react";
import FileUpload from "@/components/FileUpload";
import { useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import usePDFContext from "@/hooks/usePDFContext";

const ANALYZE_PATH = "/analyze";

const Upload = () => {
  const navigate = useNavigate();
  const context = usePDFContext();

  const handleFileSelect = useCallback(
    (file: File) => {
      if (file.type !== "application/pdf") {
        toast.error("Only PDF files are supported");
        return;
      }
      context.setCurrentPdf(file);
    },
    [context]
  );

  useEffect(() => {
    if (context.currentPdf) {
      navigate(ANALYZE_PATH);
    }
  }, [context.currentPdf, navigate]);

  return (
    <div className="flex min-h-screen w-screen justify-center">
      <div className="flex flex-col w-full max-w-7xl p-8 space-y-7">
        <h1 className="text-3xl font-bold text-center">Resume Parser</h1>
        <FileUpload onFileSelect={handleFileSelect} />
        <div className="flex gap-x-8 font-light">
          <p className="flex-grow max-w-[50%]">
            Resume Parser is a tool that converts your resume from PDF or images
            to structured output. Come with free AI-powered resume analysis.
          </p>
          <ul className="flex flex-col space-y-2 ml-auto">
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
      </div>
    </div>
  );
};

export default Upload;
