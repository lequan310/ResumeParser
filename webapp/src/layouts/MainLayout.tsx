import Sidebar from "./components/Sidebar";
import SidebarItem from "../components/SidebarItem";
import { History, LayoutDashboard } from "lucide-react";

const MainLayout = () => {
  return (
    <main className="main">
      <Sidebar>
        <SidebarItem
          icon={<LayoutDashboard size={20} />}
          text="Dashboard"
          alert
          active
        ></SidebarItem>
        <SidebarItem
          icon={<History size={20} />}
          text="History"
          alert
        ></SidebarItem>
      </Sidebar>
    </main>
  );
};

export default MainLayout;
