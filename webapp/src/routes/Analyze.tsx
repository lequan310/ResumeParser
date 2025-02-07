import { useState } from "react";
import PDFViewer from "@/components/PDFViewer";
import SplitLayout from "@/layouts/SplitLayout";
import SpinLoader from "@/components/SpinLoader";

const Parse = () => {
  const [jobDescription, setJobDescription] = useState<string>("");

  return (
    <SplitLayout
      sections={[
        <PDFViewer />,
        <div className="flex flex-col w-full h-full p-4">
          <h2 className="text-xl font-semibold mb-4">Job Description</h2>
          <textarea
            className="w-full h-full p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600 resize-none"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />
        </div>,
        <div className="flex flex-col items-center justify-center w-full h-full gap-4">
          <SpinLoader size={100} />
          <p className="text-xl animate-pulse">In development...</p>
        </div>,
      ]}
    />
  );
};

export default Parse;
