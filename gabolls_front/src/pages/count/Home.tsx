import MainLogo from '../../molecules/MainLogo';
import RulesButton from '../../organisms/RulesButton';
import StartButtons from '../../organisms/StartButtons';

const Home = () => {
    return (
        <div className='h-screen bg-background1 bg-no-repeat bg-cover bg-center bg-fixed'>
            <RulesButton />
            <MainLogo />
            <StartButtons />
        </div>
    );
};

export default Home;
