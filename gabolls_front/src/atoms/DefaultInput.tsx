type DefaultInputProps = {
    placeholder: string;
    className?: string;
    onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
};

const DefaultInput = ({ placeholder, onChange }: DefaultInputProps) => {
    return (
        <input
            type='text'
            placeholder={placeholder}
            className='input input-bordered w-full max-w-xs'
            onChange={onChange}
        />
    );
};

export default DefaultInput;
