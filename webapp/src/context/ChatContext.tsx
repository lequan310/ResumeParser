import { createContext } from "react";
import { ChatMessage } from "@/types/message";

export interface Chat {
  thread_id: string;
  messages: ChatMessage[];
}

export interface ChatContextType {
  chat: Chat;
  addMessage: (message: ChatMessage) => void;
  editLastMessage: (message: ChatMessage) => void;
  resetChat: () => void;
}

export const ChatContext = createContext<ChatContextType | undefined>(
  undefined
);
