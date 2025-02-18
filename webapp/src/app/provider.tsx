import { useState, ReactNode } from "react";
import { PDFContext, PDFFile } from "@/context/PDFContext";
import { NavContext, NavTab } from "@/context/NavContext";
import { ChatContext, Chat } from "@/context/ChatContext";
import { ResumeContext } from "@/context/ResumeContext";
import { AnalysisContext } from "@/context/AnalysisContext";
import { ChatMessage } from "@/types/message";
import { Resume } from "@/types/resume";
import { Analysis } from "@/types/analysis";
import { LoadingState } from "@/types/state";

const NavContextProvider = ({ children }: { children: ReactNode }) => {
  const [activeTab, setActiveTab] = useState<NavTab>("upload");

  return (
    <NavContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </NavContext.Provider>
  );
};

const PDFContextProvider = ({ children }: { children: ReactNode }) => {
  const [currentPdf, setCurrentPdf] = useState<PDFFile>(null);

  return (
    <PDFContext.Provider value={{ currentPdf, setCurrentPdf }}>
      {children}
    </PDFContext.Provider>
  );
};

const ChatContextProvider = ({ children }: { children: ReactNode }) => {
  const generateThreadId = () => {
    const new_thread_id = crypto.randomUUID().toString();
    return new_thread_id;
  };

  const [chat, setChat] = useState<Chat>(() => ({
    thread_id: generateThreadId(), // This will only be called once
    messages: [{ text: "Welcome! How can I help you today?", isUser: false }],
  }));

  const addMessage = (message: ChatMessage) => {
    setChat((prevChat) => ({
      ...prevChat,
      messages: [...prevChat.messages, message],
    }));
  };

  const editLastMessage = (message: ChatMessage) => {
    setChat((prevChat) => {
      const newMessages = [...prevChat.messages];
      newMessages[newMessages.length - 1] = message;
      return {
        ...prevChat,
        messages: newMessages,
      };
    });
  };

  const resetChat = () => {
    setChat({
      thread_id: generateThreadId(),
      messages: [{ text: "Welcome! How can I help you today?", isUser: false }],
    });
  };

  return (
    <ChatContext.Provider
      value={{ chat, addMessage, editLastMessage, resetChat }}
    >
      {children}
    </ChatContext.Provider>
  );
};

const ResumeContextProvider = ({ children }: { children: ReactNode }) => {
  const [parsingState, setParsingState] = useState<LoadingState>("idle");
  const [markdown, setMarkdown] = useState<string>("");
  const [resume, setResume] = useState<Resume | null>(null);

  return (
    <ResumeContext.Provider
      value={{
        parsingState,
        markdown,
        resume,
        setParsingState,
        setMarkdown,
        setResume,
      }}
    >
      {children}
    </ResumeContext.Provider>
  );
};

const AnalysisContextProvider = ({ children }: { children: ReactNode }) => {
  const [job_desc, setJobDesc] = useState<string>("");
  const [analysisState, setAnalysisState] = useState<LoadingState>("idle");
  const [analysis, setAnalysis] = useState<Analysis | null>(null);

  return (
    <AnalysisContext.Provider
      value={{
        job_desc,
        analysisState,
        analysis,
        setJobDesc,
        setAnalysisState,
        setAnalysis,
      }}
    >
      {children}
    </AnalysisContext.Provider>
  );
};

export const AppProviders = ({ children }: { children: ReactNode }) => {
  return (
    <ResumeContextProvider>
      <AnalysisContextProvider>
        <ChatContextProvider>
          <NavContextProvider>
            <PDFContextProvider>{children}</PDFContextProvider>
          </NavContextProvider>
        </ChatContextProvider>
      </AnalysisContextProvider>
    </ResumeContextProvider>
  );
};
