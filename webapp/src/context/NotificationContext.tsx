import { createContext } from "react";

export interface NotificationContextType {
  notified: boolean;
  setNotified: (notified: boolean) => void;
}

export const NotificationContext = createContext<
  NotificationContextType | undefined
>(undefined);
