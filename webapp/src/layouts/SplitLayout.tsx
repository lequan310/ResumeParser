import { ReactNode, useState, useCallback, MouseEvent } from "react";
import { GripVertical } from "lucide-react";

const SplitLayout = ({
  left,
  right,
}: {
  left: ReactNode;
  right: ReactNode;
}) => {
  const [isDragging, setIsDragging] = useState(false);
  const [leftWidth, setLeftWidth] = useState(50);

  const handleMouseDown = () => {
    setIsDragging(true);
  };

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging) {
        const container = e.currentTarget as HTMLElement;
        const newWidth = (e.clientX / container.offsetWidth) * 100;
        setLeftWidth(Math.min(Math.max(20, newWidth), 80)); // Min 20%, Max 80%
      }
    },
    [isDragging]
  );

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  return (
    <div
      className="flex w-full h-[calc(100vh-64px)]"
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
    >
      <div
        className="overflow-auto hover:overflow-auto scrollbar-thin h-full p-4 min-w-fit"
        style={{ width: `${leftWidth}%` }}
      >
        {left}
      </div>
      <div
        className="w-1.5 bg-slate-700 cursor-col-resize hover:bg-slate-600 active:bg-slate-500 flex items-center justify-center transition-colors"
        onMouseDown={handleMouseDown}
      >
        <GripVertical className="h-8 w-8 text-slate-400" />
      </div>
      <div
        className="overflow-auto hover:overflow-auto scrollbar-thin h-full p-4"
        style={{ width: `${100 - leftWidth}%` }}
      >
        {right}
      </div>
    </div>
  );
};

export default SplitLayout;
