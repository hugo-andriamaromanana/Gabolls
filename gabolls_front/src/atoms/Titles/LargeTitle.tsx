import DefaultTitle from './DefaultTitle';

type LargeTitleProps = {
    title: string;
};

const LargeTitle = ({ title }: LargeTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-5xl md:text-6xl lg:text-8xl xl:text-10xl'
        />
    );
};

export default LargeTitle;
