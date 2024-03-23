import LargeTitle from '../atoms/Titles/LargeTitle';
import MainTitle from '../atoms/Titles/MainTitle';
import MediumTitle from '../atoms/Titles/MediumTitle';
import SmallTitle from '../atoms/Titles/SmallTitle';
import TinyTitle from '../atoms/Titles/TinyTitle';

type TitleProps = {
    title: string;
    size: 'main' | 'large' | 'medium' | 'small' | 'tiny';
};

const Title = ({ title, size }: TitleProps) => {
    return (
        <div>
            {size === 'main' ? (
                <MainTitle title={title} />
            ) : size === 'large' ? (
                <LargeTitle title={title} />
            ) : size === 'medium' ? (
                <MediumTitle title={title} />
            ) : size === 'small' ? (
                <SmallTitle title={title} />
            ) : (
                <TinyTitle title={title} />
            )}
        </div>
    );
};

export default Title;
