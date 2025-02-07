import { ReactNode, useState, useCallback, MouseEvent, Fragment } from "react";
import { GripVertical } from "lucide-react";

interface SplitLayoutProps {
  sections: ReactNode[];
}

const SplitLayout = ({ sections }: SplitLayoutProps) => {
  const [isDragging, setIsDragging] = useState<number | null>(null);
  const [widths, setWidths] = useState<number[]>(() => {
    const equalWidth = 100 / sections.length;
    return Array(sections.length).fill(equalWidth);
  });

  const handleMouseDown = (index: number) => {
    setIsDragging(index);
  };

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging !== null) {
        const container = e.currentTarget as HTMLElement;
        const containerWidth = container.offsetWidth;
        const newPosition = (e.clientX / containerWidth) * 100;

        setWidths((prevWidths) => {
          const newWidths = [...prevWidths];
          const minWidth = 20;

          const delta =
            newPosition -
            newWidths.slice(0, isDragging + 1).reduce((a, b) => a + b, 0);

          if (
            newWidths[isDragging] + delta < minWidth ||
            newWidths[isDragging + 1] - delta < minWidth
          ) {
            return prevWidths;
          }

          newWidths[isDragging] += delta;
          newWidths[isDragging + 1] -= delta;

          return newWidths;
        });
      }
    },
    [isDragging]
  );

  const handleMouseUp = () => {
    setIsDragging(null);
  };

  return (
    <div
      className="flex w-full h-[calc(100vh-64px)]"
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
    >
      {sections.map((section, index) => (
        <Fragment key={`section-${index}`}>
          <div
            key={`section-${index}`}
            className="overflow-auto hover:overflow-auto scrollbar-thin h-full p-4 min-w-fit"
            style={{ width: `${widths[index]}%` }}
          >
            {section}
          </div>
          {index < sections.length - 1 && (
            <div
              key={`divider-${index}`}
              className="w-1.5 bg-slate-700 cursor-col-resize hover:bg-slate-600 active:bg-slate-500 flex items-center justify-center transition-colors"
              onMouseDown={() => handleMouseDown(index)}
            >
              <GripVertical className="h-8 w-8 text-slate-400" />
            </div>
          )}
        </Fragment>
      ))}
    </div>
  );
};

export default SplitLayout;
