import { useNavigate } from 'react-router-dom';
import CancelButton from '../../molecules/CancelButton';
import MediumTitle from '../../atoms/Titles/MediumTitle';
import DefaultButton from '../../atoms/Buttons/DefaultButton';
import GameSelector from '../../organisms/GameSelector';
import { useState } from 'react';
import DefaultInput from '../../atoms/DefaultInput';

const GameSelection = () => {
    const [name, setName] = useState('');
    const navigate = useNavigate();

    return (
        <div className='h-screen bg-quinary'>
            <CancelButton type='x' onClick={() => navigate('/')} />
            <div className='absolute justify-center top-1/4 left-1/2 -translate-y-10'>
                <MediumTitle title='Select a game' />
            </div>
            <div className='flex flex-col h-full justify-center items-center pt-12'>
                <div className='flex w-10/12 h-4/6 justify-center items-center overflow-y-auto mt-6'>
                    <GameSelector />
                </div>
                <div className='flex flex-col items-center'>
                    <DefaultInput
                        placeholder='New game'
                        onChange={e => setName(e.target.value)}
                    />
                    <DefaultButton
                        title='New game'
                        className='bg-gradient-to-r from-primary to-secondary w-fit h-12 mt-6'
                        onClick={() => navigate('/count/players')}
                    />
                </div>
            </div>
        </div>
    );
};

export default GameSelection;
