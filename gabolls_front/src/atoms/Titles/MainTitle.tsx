import DefaultTitle from './DefaultTitle';

type MainTitleProps = {
    title: string;
};

const MainTitle = ({ title }: MainTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-6xl md:text-8xl lg:text-9xl xl:text-10xl'
        />
    );
};

export default MainTitle;
