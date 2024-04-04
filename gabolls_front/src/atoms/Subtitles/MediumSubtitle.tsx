import DefaultSubtitle from "./DefaultSubtitle";


type MediumSubtitleProps = {
    title: string;
};

const MediumSubtitle = ({ title }: MediumSubtitleProps) => {
    return (
        <DefaultSubtitle
            title={title}
            className='text-mg md:text-lg lg:text-2xl xl:text-3xl'
        />
    );
};

export default MediumSubtitle;
