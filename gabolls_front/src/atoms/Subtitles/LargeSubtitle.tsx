import DefaultSubtitle from "./DefaultSubtitle";


type LargeSubtitleProps = {
    title: string;
};

const LargeSubtitle = ({ title }: LargeSubtitleProps) => {
    return (
        <DefaultSubtitle
            title={title}
            className='text-lg md:text-xl lg:text-3xl xl:text-4xl'
        />
    );
};

export default LargeSubtitle;
