import { useNavigate } from 'react-router-dom';
import DefaultButton from '../atoms/Buttons/DefaultButton';

const RulesButton = () => {
    const navigate = useNavigate();

    return (
        <div className='absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-32'>
            <DefaultButton
                title='Rules'
                className='bg-gradient-to-r from-primary to-secondary'
                onClick={() => navigate('/rules')}
            />
        </div>
    );
};

export default RulesButton;
