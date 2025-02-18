import { useState, useEffect, ReactNode, useRef } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";

interface AnalysisFieldProps {
  value?: string;
  icon?: ReactNode;
  additionalInfo?: string;
  tooltip?: string;
}

const AnalysisField = ({
  value,
  icon,
  additionalInfo,
  tooltip,
}: AnalysisFieldProps) => {
  const [inputValue, setInputValue] = useState<string>(value || "");
  const [additionalInfoValue, setAdditionalInfoValue] = useState<string>(
    additionalInfo || ""
  );
  const [isExpanded, setIsExpanded] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const reasoningRef = useRef<HTMLTextAreaElement>(null);

  const onValueChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
  };

  const onAdditionalInfoChange = (
    e: React.ChangeEvent<HTMLTextAreaElement>
  ) => {
    setAdditionalInfoValue(e.target.value);
  };

  const adjustHeight = (element: HTMLTextAreaElement) => {
    element.style.height = "auto";
    element.style.height = `${element.scrollHeight}px`;
  };

  useEffect(() => {
    setInputValue(value || "");

    if (textareaRef.current) {
      adjustHeight(textareaRef.current);
    }

    if (reasoningRef.current) {
      adjustHeight(reasoningRef.current);
    }
  }, [value]);

  useEffect(() => {
    if (isExpanded && reasoningRef.current) {
      adjustHeight(reasoningRef.current);
    }
  }, [isExpanded]);

  return (
    <div className="flex flex-col">
      <div className="relative">
        <textarea
          ref={textareaRef}
          className="w-full pr-12 outline-none border-none resize-none overflow-hidden"
          value={inputValue}
          onChange={onValueChange}
          readOnly
          rows={1}
          onInput={(e) => adjustHeight(e.target as HTMLTextAreaElement)}
        />
        <div className="absolute right-2 top-1/2 -translate-y-1/2 text-zinc-400 pb-1.25">
          <div className="relative group">
            {icon}
            {/* Tooltip */}
            {tooltip ? (
              <span className="absolute -bottom-8 -translate-x-1/2 whitespace-nowrap rounded-md bg-zinc-700 px-2 py-1 text-xs text-zinc-100 opacity-0 transition-opacity group-hover:opacity-100">
                {tooltip}
              </span>
            ) : null}
          </div>
        </div>
      </div>
      {additionalInfo && (
        <div>
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="flex items-center text-sm text-zinc-400 hover:text-zinc-300"
          >
            {isExpanded ? (
              <ChevronUp className="w-4 h-4 mr-1" />
            ) : (
              <ChevronDown className="w-4 h-4 mr-1" />
            )}
            Reasoning
          </button>
          {isExpanded && (
            <textarea
              ref={reasoningRef}
              className="w-full pt-2 pr-12 outline-none border-none resize-none overflow-hidden text-sm"
              value={additionalInfoValue}
              readOnly
              rows={1}
              onChange={onAdditionalInfoChange}
              onInput={(e) => adjustHeight(e.target as HTMLTextAreaElement)}
            />
          )}
        </div>
      )}
    </div>
  );
};

export default AnalysisField;
