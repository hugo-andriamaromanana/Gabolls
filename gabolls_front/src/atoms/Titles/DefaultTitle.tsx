type DefaultTitleProps = {
    title: string;
    className: string;
};

const DefaultTitle = ({ title, className }: DefaultTitleProps) => {
    return (
        <div className='relative'>
            <h1
                className={`absolute -top-1 -left-1 -translate-x-1/2 -translate-y-1/2 font-bold text-primary ${className}`}
            >
                {title}
            </h1>
            <h1
                className={`absolute top-1 left-1 -translate-x-1/2 -translate-y-1/2 font-bold text-secondary ${className}`}
            >
                {title}
            </h1>
            <h1
                className={`absolute top-0 -translate-x-1/2 -translate-y-1/2 font-bold text-quartenary ${className}`}
            >
                {title}
            </h1>
        </div>
    );
};

export default DefaultTitle;
