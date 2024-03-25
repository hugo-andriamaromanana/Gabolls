import PlayButton from '../molecules/PlayButton';
import CountButton from '../molecules/CountButton';

const StartButtons = () => {
    return (
        <div className='absolute top-3/4 left-1/2 -translate-x-1/2 translate-y-16'>
            <div className='flex justify-between h-14 sm:h-24 md:h-28 lg:h-32'>
                <PlayButton />
                <div />
                <CountButton />
            </div>
        </div>
    );
};

export default StartButtons;
