import DefaultButton from '../atoms/Buttons/DefaultButton';

const Authentification = ({ onClick }: { onClick: () => void }) => {
    return (
        <div className='absolute top-8 right-8'>
            <DefaultButton
                title=':)'
                className='bg-gradient-to-r from-primary to-secondary rounded-full w-fit h-fit border-none'
                onClick={onClick}
            />
        </div>
    );
};

export default Authentification;
