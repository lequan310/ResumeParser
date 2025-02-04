interface SpinLoaderProps {
  size?: number;
  color?: string;
}

const SpinLoader = ({ size = 40, color = "#1976d2" }: SpinLoaderProps) => {
  return (
    <div className="flex items-center justify-center">
      <div
        className={`inline-block rounded-full border-opacity-20 animate-spin`}
        style={{
          width: size,
          height: size,
          borderWidth: size / 10,
          borderTopColor: color,
          borderRightColor: `${color}20`,
          borderBottomColor: `${color}20`,
          borderLeftColor: `${color}20`,
        }}
      />
    </div>
  );
};

export default SpinLoader;
