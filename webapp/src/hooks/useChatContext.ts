import { useContext } from "react";
import { ChatContext } from "@/context/ChatContext";

const useChatContext = () => {
    const context = useContext(ChatContext);

    if (context === undefined) {
        throw new Error("useChatContext must be used within a ChatProvider");
    }

    return context;
};

export default useChatContext;
