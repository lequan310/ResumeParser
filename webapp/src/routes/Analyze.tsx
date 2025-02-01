import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import ResumeForm from "@/components/resume-form/ResumeForm";

const Analyze = () => {
  return <SplitLayout left={<PDFViewer />} right={<ResumeForm />} />;
};

export default Analyze;
