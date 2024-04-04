type DefaultSubtitleProps = {
    title: string;
    className: string;
};

const DefaultSubtitle = ({ title, className }: DefaultSubtitleProps) => {
    return (
        <div className='relative'>
            <h3
                className={`absolute w-max flex justify-center -top-0.5 -left-0.5 -translate-x-1/3 -translate-y-1/2 font-bold text-primary ${className}`}
            >
                {title}
            </h3>
            <h3
                className={`absolute w-max flex justify-center top-0.5 left-0.5 -translate-x-1/3 -translate-y-1/2 font-bold text-secondary ${className}`}
            >
                {title}
            </h3>
            <h3
                className={`absolute w-max flex justify-center top-0 -translate-x-1/3 -translate-y-1/2 font-bold text-quartenary ${className}`}
            >
                {title}
            </h3>
        </div>
    );
};

export default DefaultSubtitle;
