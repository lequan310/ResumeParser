import { useState, useEffect } from "react";

interface FormInputProps {
  label?: string;
  placeholder?: string;
  multiline?: boolean;
  value?: string;
}

const FormInput = ({
  label,
  placeholder,
  multiline,
  value,
}: FormInputProps) => {
  const [inputValue, setInputValue] = useState<string>(value || "");

  const onChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setInputValue(e.target.value);
  };

  useEffect(() => {
    setInputValue(value || "");
  }, [value]);

  return (
    <div className="flex flex-col gap-1">
      <label className="text-base font-semibold text-zinc-200">{label}</label>
      {multiline ? (
        <textarea
          placeholder={placeholder}
          rows={4}
          className="p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600"
          value={inputValue}
          onChange={onChange}
        />
      ) : (
        <input
          type="text"
          placeholder={placeholder}
          className="p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600"
          value={inputValue}
          onChange={onChange}
        />
      )}
    </div>
  );
};

export default FormInput;
