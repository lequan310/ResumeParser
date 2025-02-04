import cvLogo from "/cv.webp";
import { useNavigate } from "react-router-dom";
import useNavContext from "@/hooks/useNavContext";
import { NavTab } from "@/context/NavContext";

const Navbar = () => {
  const navContext = useNavContext();
  const navigate = useNavigate();

  const navigateOnClick = (path: NavTab) => {
    navContext.setActiveTab(path);
    navigate(`/${path}`);
  };

  const logoOnClick = () => {
    navigateOnClick("parse");
  };

  const parseOnClick = () => {
    navigateOnClick("parse");
  };

  const analyzeOnClick = () => {
    navigateOnClick("analyze");
  };

  const historyOnClick = () => {
    navigateOnClick("history");
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
            onClick={parseOnClick}
          >
            Parse
          </span>
          <span
            className={`text-white cursor-pointer hover:text-blue-200 ${
              navContext.activeTab === "analyze" ? "font-bold" : ""
            }`}
            onClick={analyzeOnClick}
          >
            Analyze
          </span>
          <span
            className={`text-white cursor-pointer hover:text-blue-200 ${
              navContext.activeTab === "history" ? "font-bold" : ""
            }`}
            onClick={historyOnClick}
          >
            History
          </span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
