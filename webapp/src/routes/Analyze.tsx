import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import { ChatButton, ChatBox } from "@/components/chat";
import ResumeForm from "@/components/resume-form/ResumeForm";
import { useState } from "react";

const Analyze = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <>
      <SplitLayout left={<PDFViewer />} right={<ResumeForm />} />
      <ChatButton onClick={() => setIsChatOpen(!isChatOpen)} />
      {isChatOpen && <ChatBox onClose={() => setIsChatOpen(false)} />}
    </>
  );
};

export default Analyze;
