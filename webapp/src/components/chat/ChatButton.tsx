import { MessageCircleMore } from "lucide-react";

const ChatButton = ({ onClick }: { onClick: () => void }) => {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-8 right-8 p-4 rounded-full bg-blue-600 hover:bg-blue-700 text-white shadow-lg"
    >
      <MessageCircleMore size={28} />
    </button>
  );
};

export default ChatButton;
