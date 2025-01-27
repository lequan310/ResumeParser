import { useContext } from "react";
import { NavContext } from "@/context/NavContext";

const useNavContext = () => {
    const context = useContext(NavContext);

    if (context === undefined) {
        throw new Error("useNavContext must be used within a NavProvider");
    }

    return context;
};

export default useNavContext;
