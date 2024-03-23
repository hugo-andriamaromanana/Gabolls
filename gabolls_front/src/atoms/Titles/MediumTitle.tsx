import DefaultTitle from './DefaultTitle';

type MediumTitleProps = {
    title: string;
};

const MediumTitle = ({ title }: MediumTitleProps) => {
    return (
        <DefaultTitle
            title={title}
            className='text-3xl md:text-4xl lg:text-6xl xl:text-10xl'
        />
    );
};

export default MediumTitle;
