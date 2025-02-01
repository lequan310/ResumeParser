import { useState } from "react";
import { Send } from "lucide-react";
import { ChatMessage } from "@/types/message";

const ChatBox = ({ onClose }: { onClose: () => void }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    { text: "Welcome! How can I help you today?", isUser: false },
  ]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, isUser: true }]);
      setInput("");
    }
  };

  return (
    <div className="fixed bottom-24 right-12 w-96 h-[32rem] bg-gray-900 rounded-lg shadow-xl border border-gray-700">
      <div className="flex justify-between items-center p-4 border-b border-gray-700">
        <h3 className="font-semibold text-gray-200">Chat</h3>
        <button onClick={onClose} className="text-gray-400 hover:text-gray-200">
          ✕
        </button>
      </div>

      <div className="p-4 h-[calc(100%-8rem)] overflow-y-auto scrollbar-thin scrollbar-thumb-gray-700">
        <div className="flex flex-col space-y-3">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${msg.isUser ? "justify-end" : "justify-start"}`}
            >
              <div
                className={`max-w-[80%] p-2.5 rounded-lg text-sm ${
                  msg.isUser
                    ? "bg-blue-600 text-white"
                    : "bg-gray-800 text-gray-200"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}
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
