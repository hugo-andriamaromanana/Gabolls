type DefaultTitleProps = {
    title: string;
    className: string;
};

const DefaultTitle = ({ title, className }: DefaultTitleProps) => {
    return (
        <div className='relative m-auto'>
            <h1
                className={`absolute -top-1 -left-1 -translate-x-1/2 -translate-y-1/2 ${className} font-bold text-primary`}
            >
                {title}
            </h1>
            <h1
                className={`absolute top-1 left-1 -translate-x-1/2 -translate-y-1/2 ${className} font-bold text-secondary`}
            >
                {title}
            </h1>
            <h1
                className={`absolute top-0 -translate-x-1/2 -translate-y-1/2 ${className} font-bold text-quartenary`}
            >
                {title}
            </h1>
        </div>
    );
};

export default DefaultTitle;
