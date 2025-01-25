import { createContext } from "react";

export type NavTab = "parse" | "analyze" | "history";

interface NavContextType {
  activeTab: NavTab;
  setActiveTab: (tab: NavTab) => void;
}

export const NavContext = createContext<NavContextType | undefined>(undefined);
