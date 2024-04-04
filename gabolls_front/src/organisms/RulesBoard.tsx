import BoardBackground from '../molecules/BoardBackground';
import RulesText from '../molecules/RulesText';

const RulesBoard = () => {
    return (
        <div className='bg-senary'>
            <BoardBackground>
                <RulesText />
            </BoardBackground>

        </div>
    );
};

export default RulesBoard;