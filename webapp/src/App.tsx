import { CircleCheck } from "lucide-react";
import FileUpload from "@/components/FileUpload";

const App = () => {
  return (
    <div className="flex min-h-screen w-screen justify-center">
      <div className="flex flex-col w-full max-w-7xl p-8 space-y-7">
        <h1 className="text-3xl font-bold text-center">Resume Parser</h1>
        <FileUpload onFileSelect={(file) => console.log(file)} />
        <div className="flex gap-x-8 font-light">
          <p className="flex-grow max-w-[50%]">
            Resume Parser is a tool that converts your resume from PDF or images
            to structured output. Come with free AI-powered resume analysis.
          </p>
          <ul className="flex flex-col space-y-2 ml-auto">
            <li className="flex items-center gap-x-2">
              <CircleCheck className="w-4 h-4 text-green-500" />
              Accurately convert resume to structured output.
            </li>
            <li className="flex items-center gap-x-2">
              <CircleCheck className="w-4 h-4 text-green-500" />
              Free, support PDF and images.
            </li>
            <li className="flex items-center gap-x-2">
              <CircleCheck className="w-4 h-4 text-green-500" />
              AI-powered analysis and recommendation.
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;
