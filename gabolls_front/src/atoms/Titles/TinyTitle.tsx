import DefaultTitle from './DefaultTitle';

type TinyTitleProps = {
    title: string;
};

const TinyTitle = ({ title }: TinyTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-xl md:text-2xl lg:text-4xl xl:text-10xl'
        />
    );
};

export default TinyTitle;
