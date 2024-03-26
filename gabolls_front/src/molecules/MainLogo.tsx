import Title from './Title';
import logo from '../assets/logo.svg';

function MainLogo() {
    return (
        <>
            <img
                alt='GABOLLS LOGO'
                className='absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 size-3/4 sm:size-1/4 md:size-1/4 lg:size-1/2'
                src={logo}
            />
            <div className='absolute top-1/2 left-1/2'>
                <Title title='GABOLLS' size='main' />
            </div>
        </>
    );
}

export default MainLogo;
