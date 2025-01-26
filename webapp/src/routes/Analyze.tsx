import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import ChatButton from "@/components/ChatButton";
import ChatBox from "@/components/ChatBox";
import { useState } from "react";

const Analyze = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <>
      <SplitLayout left={<PDFViewer />} right={null} />
      <ChatButton onClick={() => setIsChatOpen(!isChatOpen)} />
      {isChatOpen && <ChatBox onClose={() => setIsChatOpen(false)} />}
    </>
  );
};

export default Analyze;
