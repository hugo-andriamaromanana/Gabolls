import DefaultTitle from './DefaultTitle';

type MediumTitleProps = {
    title: string;
};

const MediumTitle = ({ title }: MediumTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-3xl md:text-4xl lg:text-5xl xl:text-7xl'
        />
    );
};

export default MediumTitle;
