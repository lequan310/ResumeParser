import { useContext } from "react";
import { NotificationContext } from "@/context/NotificationContext";

const useNotificationContext = () => {
    const context = useContext(NotificationContext);

    if (context === undefined) {
        throw new Error(
            "useNotificationContext must be used within a NotificationProvider"
        );
    }

    return context;
};

export default useNotificationContext;
