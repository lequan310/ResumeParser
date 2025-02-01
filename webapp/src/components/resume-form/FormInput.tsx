interface FormInputProps {
  label?: string;
  placeholder?: string;
  multiline?: boolean;
}

const FormInput = ({ label, placeholder, multiline }: FormInputProps) => {
  return (
    <div className="flex flex-col gap-1">
      <label className="text-base font-semibold text-zinc-200">{label}</label>
      {multiline ? (
        <textarea
          placeholder={placeholder}
          rows={4}
          className="p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600"
        />
      ) : (
        <input
          type="text"
          placeholder={placeholder}
          className="p-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600"
        />
      )}
    </div>
  );
};

export default FormInput;
