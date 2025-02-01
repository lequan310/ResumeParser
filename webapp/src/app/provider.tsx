import { useState, ReactNode } from "react";
import { PDFContext, PDFFile } from "@/context/PDFContext";
import { NavContext, NavTab } from "@/context/NavContext";
import { ChatContext, Chat } from "@/context/ChatContext";
import { ChatMessage } from "@/types/message";

const NavContextProvider = ({ children }: { children: ReactNode }) => {
  const [activeTab, setActiveTab] = useState<NavTab>("parse");

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
    console.log(new_thread_id);
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

export const AppProviders = ({ children }: { children: ReactNode }) => {
  return (
    <ChatContextProvider>
      <NavContextProvider>
        <PDFContextProvider>{children}</PDFContextProvider>
      </NavContextProvider>
    </ChatContextProvider>
  );
};
