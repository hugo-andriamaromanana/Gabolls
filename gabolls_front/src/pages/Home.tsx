import Title from '../molecules/Title';
import logo from '../assets/logo.svg';
import DefaultButton from '../atoms/Buttons/DefaultButton';
import PlayButton from '../molecules/PlayButton';
import CountButton from '../molecules/CountButton';

const Home = () => {
    return (
        <div className='h-screen bg-background1 bg-no-repeat bg-cover bg-center bg-fixed'>
            <div className='absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-32'>
                <DefaultButton
                    title='Rules'
                    className='bg-gradient-to-r from-primary to-secondary'
                />
            </div>
            <img
                className='absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 size-3/4 sm:size-1/4 md:size-1/4 lg:size-1/2'
                src={logo}
            />
            <div className='absolute top-1/2 left-1/2'>
                <Title title='GABOLLS' size='main' />
            </div>
            <div className='absolute top-3/4 left-1/2 -translate-x-1/2 translate-y-16'>
                <div className='flex justify-between h-14 sm:h-24 md:h-28 lg:h-32'>
                    <PlayButton />
                    <div />
                    <CountButton />
                </div>
            </div>
        </div>
    );
};

export default Home;
