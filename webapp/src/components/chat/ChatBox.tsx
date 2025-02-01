import { useState, useRef, useEffect } from "react";
import { Send } from "lucide-react";
import useChatContext from "@/hooks/useChatContext";
import chatService from "@/services/chatService";

const ChatBox = ({ onClose }: { onClose: () => void }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatContext = useChatContext();
  const [input, setInput] = useState("");

  const handleSend = async () => {
    const trimmedInput = input.trim();
    if (trimmedInput) {
      chatContext.addMessage({ text: input, isUser: true });
      setInput("");
      chatContext.addMessage({ text: "", isUser: false, isTyping: true });

      // Retrieve response from chat service
      let accumulatedText = "";
      for await (const chunk of chatService.sendMessage(
        trimmedInput,
        chatContext.chat.thread_id
      )) {
        accumulatedText += chunk;
        chatContext.editLastMessage({
          text: accumulatedText,
          isUser: false,
          isTyping: false,
        });
      }
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatContext.chat.messages]);

  // Add typing indicator component
  const TypingIndicator = () => (
    <div className="flex space-x-2 p-2">
      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.2s]" />
      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.4s]" />
    </div>
  );

  return (
    <div className="fixed bottom-28 right-14 w-108 h-[32rem] bg-gray-900 rounded-lg shadow-xl border border-gray-700">
      <div className="flex justify-between items-center p-4 border-b border-gray-700">
        <h3 className="font-semibold text-gray-200">Chat</h3>
        <button onClick={onClose} className="text-gray-400 hover:text-gray-200">
          ✕
        </button>
      </div>

      <div className="p-4 h-[calc(100%-8rem)] overflow-y-auto scrollbar-thin scrollbar-thumb-gray-700">
        <div className="flex flex-col space-y-3">
          {chatContext.chat.messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${
                message.isUser ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[80%] rounded-lg p-2.5 m-1 ${
                  message.isUser ? "bg-blue-600" : "bg-gray-700"
                }`}
              >
                {message.isTyping ? <TypingIndicator /> : message.text}
              </div>
            </div>
          ))}

          {/* Scroll to bottom */}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className="absolute bottom-0 left-0 right-0 p-3 border-t border-gray-700">
        <div className="flex items-center gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-1 bg-gray-800 text-gray-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type a message..."
          />
          <button
            onClick={handleSend}
            className="p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center justify-center"
          >
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatBox;
