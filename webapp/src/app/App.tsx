import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Upload, Analyze, History } from "@/routes";
import { AppProviders } from "@/app/provider";
import Navbar from "@/components/Navbar";

const App = () => {
  return (
    <AppProviders>
      <BrowserRouter>
        <Navbar />
        <div className="pt-16 w-screen">
          <Routes>
            <Route index element={<Upload />} />
            <Route path="/parse" element={<Upload />} />
            <Route path="/analyze" element={<Analyze />} />
            <Route path="/history" element={<History />} />
          </Routes>
        </div>
      </BrowserRouter>
    </AppProviders>
  );
};

export default App;
