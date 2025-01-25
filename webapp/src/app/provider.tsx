import { useState, ReactNode } from "react";
import { PDFContext, PDFFile } from "@/context/PDFContext";
import { NavContext, NavTab } from "@/context/NavContext";

const NavContextProvider = ({ children }: { children: ReactNode }) => {
  const [activeTab, setActiveTab] = useState<NavTab>("parse");

  return (
    <NavContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </NavContext.Provider>
  );
};

const PDFContextProvider = ({ children }: { children: ReactNode }) => {
  const [currentPdf, setCurrentPdf] = useState<PDFFile>(null);

  return (
    <PDFContext.Provider value={{ currentPdf, setCurrentPdf }}>
      {children}
    </PDFContext.Provider>
  );
};

export const AppProviders = ({ children }: { children: ReactNode }) => {
  return (
    <NavContextProvider>
      <PDFContextProvider>{children}</PDFContextProvider>
    </NavContextProvider>
  );
};
