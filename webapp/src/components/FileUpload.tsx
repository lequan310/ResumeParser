import { UploadIcon } from "lucide-react";
import React, { ChangeEvent, useState } from "react";

interface FileUploadProps {
  onFileSelect: (file: File) => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ onFileSelect }) => {
  const [dragActive, setDragActive] = useState(false);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onFileSelect(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    if (e.target.files && e.target.files.length > 0) {
      onFileSelect(e.target.files[0]);
    }
  };

  return (
    <div
      className={`w-full max-w mx-auto p-16 border-2 border-dashed rounded-lg ${
        dragActive ? "border-blue-500" : "border-gray-300"
      } transition-colors duration-300 ease-in-out`}
      onDragEnter={handleDrag}
      onDragLeave={handleDrag}
      onDragOver={handleDrag}
      onDrop={handleDrop}
    >
      <label className="flex flex-col items-center justify-center h-full space-y-4 cursor-pointer">
        <UploadIcon className="w-12 h-12 text-gray-400 stroke-2" />
        <div className="text-center">
          <p className="text-lg font-medium text-gray-300">
            Drop your files here, or
            <span className="text-blue-500 hover:text-blue-600"> browse</span>
          </p>
          <p className="text-sm text-gray-100">Supported files: PDF</p>
        </div>
        <input
          type="file"
          className="hidden"
          onChange={handleChange}
          accept=".pdf"
          multiple={false}
        />
      </label>
    </div>
  );
};

export default FileUpload;
