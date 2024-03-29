type DefaultButtonProps = {
    title?: string;
    className?: string;
    children?: React.ReactNode;
    onClick?: () => void;
};

const DefaultButton = ({
    title,
    className,
    children,
    onClick
}: DefaultButtonProps) => {
    return (
        <button
            className={`btn h-full mx-4 w-32 shadow-lg rounded-xl border-none shadow-quinary text-quartenary text-xl font-bold hover:scale-110 transition-transform duration-300 ease-in-out ${className}`}
            onClick={onClick}
        >
            {title}
            {children}
        </button>
    );
};

export default DefaultButton;
