import AnalysisField from "@/components/analysis-form/AnalysisField";
import { CircleCheck, CircleHelp, CircleX } from "lucide-react";
import { useAnalysisContext } from "@/hooks";

interface AnalysisFormProps {
  analyzeOnClick: () => void;
}

const AnalysisForm: React.FC<AnalysisFormProps> = ({ analyzeOnClick }) => {
  const analysisContext = useAnalysisContext();

  return (
    <div className="h-full p-6">
      <div className="space-y-12 h-full">
        {/* Basic Requirements */}
        <div className="min-h-[calc(40%)] space-y-8">
          <h2 className="text-3xl font-bold mb-4 text-gray-100">
            Basic Requirements
          </h2>
          {analysisContext.analysis?.basic_requirement_checks.map(
            (requirement, index) => (
              <AnalysisField
                key={index}
                value={`${index + 1}.    ${requirement.requirement}`}
                additionalInfo={requirement.thinking}
                icon={
                  requirement.is_present === "YES" ? (
                    <CircleCheck className="text-green-500" />
                  ) : requirement.is_present === "NO" ? (
                    <CircleX className="text-red-600" />
                  ) : (
                    <CircleHelp />
                  )
                }
                tooltip={
                  requirement.is_present === "YES"
                    ? "Requirement met"
                    : requirement.is_present === "NO"
                    ? "Requirement not met"
                    : "Require human screening"
                }
              />
            )
          )}
        </div>

        {/* Preferred Requirements */}
        <div className="min-h-[calc(40%)] space-y-8">
          <h2 className="text-3xl font-bold mb-4 text-gray-100">
            Preferred Requirements
          </h2>
          {analysisContext.analysis?.preferred_requirement_checks.map(
            (requirement, index) => (
              <AnalysisField
                key={index}
                value={`${index + 1}.    ${requirement.requirement}`}
                additionalInfo={requirement.thinking}
                icon={
                  requirement.is_present === "YES" ? (
                    <CircleCheck className="text-green-500" />
                  ) : requirement.is_present === "NO" ? (
                    <CircleX className="text-red-600" />
                  ) : (
                    <CircleHelp />
                  )
                }
                tooltip={
                  requirement.is_present === "YES"
                    ? "Requirement met"
                    : requirement.is_present === "NO"
                    ? "Requirement not met"
                    : "Require human screening"
                }
              />
            )
          )}
        </div>

        {/* Analyze Button */}
        <div className="flex justify-center">
          <button
            onClick={analyzeOnClick}
            className="px-6 py-2 mb-6 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors duration-200"
          >
            Analyze Resume
          </button>
        </div>
      </div>
    </div>
  );
};

export default AnalysisForm;
