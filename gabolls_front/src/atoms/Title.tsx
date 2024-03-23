type TitleProps = {
    title: string;
    size: 'main' | 'large' | 'medium' | 'small' | 'tiny';
};

const Title = ({ title }: TitleProps) => {
    return (
        <div className='relative'>
            <h1 className='absolute top-0 text-5xl font-bold text-primary drop'>
                {title}
            </h1>
            <h1 className='absolute top-2 text-5xl font-bold text-secondary drop'>
                {title}
            </h1>
            <h1 className='absolute top-1 text-5xl font-bold text-quartenary drop'>
                {title}
            </h1>
        </div>
    );
};

export default Title;
