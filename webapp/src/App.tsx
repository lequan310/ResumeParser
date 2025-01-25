import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Upload, Analyze, History } from "@/routes";
import { PDFContext } from "@/context/PDFContext";
import { useState } from "react";
import type { PDFFile } from "@/context/PDFContext";

const App = () => {
  const [currentPdf, setCurrentPdf] = useState<PDFFile>(null);

  return (
    <PDFContext.Provider value={{ currentPdf, setCurrentPdf }}>
      <BrowserRouter>
        <Routes>
          <Route index element={<Upload />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/analyze" element={<Analyze />} />
          <Route path="/history" element={<History />} />
        </Routes>
      </BrowserRouter>
    </PDFContext.Provider>
  );
};

export default App;
