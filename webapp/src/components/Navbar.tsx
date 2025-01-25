import cvLogo from "/cv.webp";
import { useNavigate } from "react-router-dom";
import usePDFContext from "@/hooks/usePDFContext";
import useNavContext from "@/hooks/useNavContext";

const Navbar = () => {
  const pdfContext = usePDFContext();
  const navContext = useNavContext();
  const navigate = useNavigate();

  const logoOnClick = () => {
    pdfContext.setCurrentPdf(null);
    navContext.setActiveTab("parse");
    navigate("/");
  };

  return (
    <nav className="fixed top-0 w-full bg-blue-600 h-16 shadow-md z-50">
      <div className="flex items-center h-full">
        <div
          className="flex items-center pl-4 cursor-pointer"
          onClick={logoOnClick}
        >
          <img src={cvLogo} width={40} height={40} className="ml-4" />
          <div className="flex flex-col ml-2">
            <p className="text-white font-bold leading-none text-lg">Resume</p>
            <p className="text-white font-bold leading-none text-lg">Parser</p>
          </div>
        </div>

        <div className="flex items-center ml-16 space-x-8">
          <span
            className={`text-white cursor-pointer hover:text-blue-200 ${
              navContext.activeTab === "parse" ? "font-bold" : ""
            }`}
            onClick={() => {
              pdfContext.setCurrentPdf(null);
              navContext.setActiveTab("parse");
              navigate("/");
            }}
          >
            Parse
          </span>
          <span
            className={`text-white cursor-pointer hover:text-blue-200 ${
              navContext.activeTab === "analyze" ? "font-bold" : ""
            }`}
            onClick={() => {
              navContext.setActiveTab("analyze");
              navigate("/analyze");
            }}
          >
            Analyze
          </span>
          <span
            className={`text-white cursor-pointer hover:text-blue-200 ${
              navContext.activeTab === "history" ? "font-bold" : ""
            }`}
            onClick={() => {
              navContext.setActiveTab("history");
              navigate("/history");
            }}
          >
            History
          </span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
