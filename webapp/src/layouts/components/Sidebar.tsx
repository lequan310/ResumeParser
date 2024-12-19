interface SidebarProps {
  children: React.ReactNode;
}

const Sidebar: React.FC<SidebarProps> = ({ children }) => {
  return (
    <aside className="h-screen">
      <nav className="h-full flex flex-col bg-white border-r shadow-sm">
        <div className="p-4 pb-2 flex justify-between items-center">
          {/* Logo here */}
        </div>

        <ul className="flex-1 px-3">{children}</ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
