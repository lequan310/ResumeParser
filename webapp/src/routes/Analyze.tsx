import PDFViewer from "@/components/PDFViewer";

const Analyze = () => {
  return (
    <div className="flex min-h-screen w-screen justify-center">
      <div className="flex flex-col w-full max-w-7xl p-8 space-y-7">
        <PDFViewer />
      </div>
    </div>
  );
};

export default Analyze;
