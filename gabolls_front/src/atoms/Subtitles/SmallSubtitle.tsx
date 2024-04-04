
import DefaultSubtitle from "./DefaultSubtitle";


type SmallSubtitleProps = {
    title: string;
};

const SmallSubtitle = ({ title }: SmallSubtitleProps) => {
    return (
        <DefaultSubtitle
            title={title}
            className='text-sg md:text-mg lg:text-xl xl:text-2xl'
        />
    );
};

export default SmallSubtitle;
