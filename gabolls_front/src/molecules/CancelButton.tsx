import DefaultButton from '../atoms/Buttons/DefaultButton';

type CancelButtonProps = {
    type: 'arrow' | 'x';
    onClick: () => void;
};

const CancelButton = ({ type, onClick }: CancelButtonProps) => {
    return (
        <div className='absolute top-8 left-8'>
            <DefaultButton
                title={type === 'arrow' ? '<' : 'X'}
                className='bg-gradient-to-r from-primary to-secondary rounded-full w-fit h-fit border-none'
                onClick={onClick}
            />
        </div>
    );
};

export default CancelButton;
