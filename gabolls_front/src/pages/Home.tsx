import Title from '../atoms/Title';

const Home = () => {
    return (
        <div className='h-screen bg-tertiary'>
            <div className='absolute top-28 right-1/2 bg-red-50'>
                <button className='btn bg-primary'>test</button>
            </div>
            <div className='absolute top-1/3 left-1/4'>
                <Title title='Gabolls' size='main' />
            </div>
            <button className='btn absolute bottom-0 right-1/2 m-4 p-2 bg-primary'>
                test
            </button>
        </div>
    );
};

export default Home;
