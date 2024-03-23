import DefaultButton from '../atoms/Buttons/DefaultButton';

type PlayButtonProps = {
    addedClass?: string;
};

const PlayButton = ({ addedClass }: PlayButtonProps) => {
    return (
        <div>
            <DefaultButton
                title={'PLAY'}
                className={`md:w-36 lg:w-96 text-2xl sm:text-3xl md:text-4xl lg:text-6xl bg-gradient-to-r from-primary to-secondary ${addedClass}`}
            />
        </div>
    );
};

export default PlayButton;
