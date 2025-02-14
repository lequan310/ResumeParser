import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import ResumeForm from "@/components/resume-form/ResumeForm";
import { LoadingState } from "@/context/ResumeContext";
import { useResumeContext } from "@/hooks";
import SpinLoader from "@/components/SpinLoader";

const Parse = () => {
  const resumeContext = useResumeContext();

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
