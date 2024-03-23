type DefaultButtonProps = {
    title: string;
    className?: string;
};

const DefaultButton = ({ title, className }: DefaultButtonProps) => {
    return (
        <button
            className={`btn h-full mx-4 w-32 shadow-lg rounded-xl shadow-quinary text-quartenary text-xl font-bold hover:scale-125 transition-transform duration-300 ease-in-out ${className}`}
        >
            {title}
        </button>
    );
};

export default DefaultButton;
