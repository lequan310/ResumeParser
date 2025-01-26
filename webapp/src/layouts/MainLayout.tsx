import { ReactNode } from "react";

const MainLayout = ({ children }: { children: ReactNode }) => {
  return (
    <div className="flex min-h-[calc(100vh-80px)] justify-center align-top">
      <div className="flex flex-col w-full max-w-7xl p-8 space-y-7">
        {children}
      </div>
    </div>
  );
};

export default MainLayout;
