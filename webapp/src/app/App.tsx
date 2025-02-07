import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Upload, Analyze, Parse } from "@/routes";
import { AppProviders } from "@/app/provider";
import { ChatButton, ChatBox } from "@/components/chat";
import { ToastContainer } from "react-toastify";
import Navbar from "@/components/Navbar";

const App = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <AppProviders>
      <ToastContainer />
      <BrowserRouter>
        <Navbar />
        <div className="pt-16 w-screen">
          <Routes>
            <Route index element={<Upload />} />
            <Route path="/upload" element={<Upload />} />
            <Route path="/parse" element={<Parse />} />
            <Route path="/analyze" element={<Analyze />} />
          </Routes>
        </div>
        <ChatButton onClick={() => setIsChatOpen(!isChatOpen)} />
        {isChatOpen && <ChatBox onClose={() => setIsChatOpen(false)} />}
      </BrowserRouter>
    </AppProviders>
  );
};

export default App;
