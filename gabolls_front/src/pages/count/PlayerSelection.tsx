import { useNavigate } from 'react-router-dom';
import CancelButton from '../../molecules/CancelButton';
import MediumTitle from '../../atoms/Titles/MediumTitle';
import PlayersForm from '../../organisms/PlayersForm';
import DefaultButton from '../../atoms/Buttons/DefaultButton';

const PlayerSelection = () => {
    const navigate = useNavigate();
    return (
        <div className='h-screen bg-quinary'>
            <CancelButton type='x' onClick={() => navigate('/')} />
            <div className='absolute w-11/12 justify-center top-1/4 left-1/2 -translate-y-10'>
                <MediumTitle title='Select players' />
            </div>
            <div className='flex flex-col h-full justify-center items-center pt-12'>
                <div className='flex w-10/12 h-4/6 justify-center items-center overflow-y-auto'>
                    <PlayersForm />
                </div>
                <div className=''>
                    <DefaultButton
                        title='START'
                        className='bg-gradient-to-r from-primary to-secondary'
                        onClick={() => navigate('/count/scores')}
                    />
                </div>
            </div>
        </div>
    );
};

export default PlayerSelection;
