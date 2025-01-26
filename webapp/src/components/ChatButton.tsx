import { MessageCircleMore } from "lucide-react";

const ChatButton = ({ onClick }: { onClick: () => void }) => {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-6 right-6 p-4 rounded-full bg-blue-500 hover:bg-blue-600 text-white shadow-lg"
    >
      <MessageCircleMore size={24} />
    </button>
  );
};

export default ChatButton;
