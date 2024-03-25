import { useNavigate } from 'react-router-dom';
import DefaultButton from '../atoms/Buttons/DefaultButton';

type CountButtonProps = {
    addedClass?: string;
};

const CountButton = ({ addedClass }: CountButtonProps) => {
    const navigate = useNavigate();

    return (
        <div>
            <DefaultButton
                title={'COUNT'}
                className={`md:w-36 lg:w-96 text-2xl sm:text-3xl md:text-4xl lg:text-6xl bg-gradient-to-r from-secondary to-primary ${addedClass}`}
                onClick={() => navigate('/count')}
            />
        </div>
    );
};

export default CountButton;
