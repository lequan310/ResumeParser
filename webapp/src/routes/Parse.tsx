import { useEffect } from "react";
import { toast } from "react-toastify";
import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import ResumeForm from "@/components/resume-form/ResumeForm";
import { LoadingState } from "@/context/ResumeContext";
import {
  useResumeContext,
  usePDFContext,
  useNotificationContext,
} from "@/hooks";
import SpinLoader from "@/components/SpinLoader";

const Parse = () => {
  const resumeContext = useResumeContext();
  const pdfContext = usePDFContext();
  const notificationContext = useNotificationContext();

  useEffect(() => {
    if (pdfContext.currentPdf && !notificationContext.notified) {
      if (resumeContext.loadingState === ("error" as LoadingState)) {
        toast.error(resumeContext.markdown);
        notificationContext.setNotified(true);
      } else if (resumeContext.loadingState === ("success" as LoadingState)) {
        toast.success(pdfContext.currentPdf.name + " parsed successfully.");
        notificationContext.setNotified(true);
      }
    }
  }, [
    resumeContext.loadingState,
    resumeContext.markdown,
    pdfContext.currentPdf,
    notificationContext,
  ]);

  return (
    <SplitLayout
      sections={[
        <PDFViewer />,
        resumeContext.loadingState === ("loading" as LoadingState) ? (
          <div className="flex flex-col items-center justify-center w-full h-full gap-4">
            <SpinLoader size={100} />
            <p className="text-xl animate-pulse">Parsing Resume...</p>
          </div>
        ) : (
          <ResumeForm />
        ),
      ]}
    />
  );
};

export default Parse;
