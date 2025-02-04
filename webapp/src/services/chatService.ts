import axiosInstance from "@/services/axiosInstance";

const chatService = {
    sendMessage: async function* (message: string, thread_id: string = "0") {
        const sentMessage = {
            message: message,
            thread_id: thread_id,
        };

        const response = await axiosInstance.post("/chat", sentMessage, {
            adapter: "fetch",
            responseType: "stream",
        });

        const reader = response.data.getReader();
        const decoder = new TextDecoder("utf-8");

        try {
            while (true) {
                const { done, value } = await reader.read();

                if (done) {
                    break;
                }

                const textChunk = decoder.decode(value, { stream: true });
                yield textChunk;
            }
        } catch (error) {
            console.error("Error reading stream:", error);
        } finally {
            reader.releaseLock(); // Important: Release the reader when done or on error
        }
    },
};

export default chatService;
