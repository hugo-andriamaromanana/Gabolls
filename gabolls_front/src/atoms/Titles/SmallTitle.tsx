import DefaultTitle from './DefaultTitle';

type SmallTitleProps = {
    title: string;
};

const SmallTitle = ({ title }: SmallTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-2xl md:text-3xl lg:text-5xl xl:text-6xl'
        />
    );
};

export default SmallTitle;
