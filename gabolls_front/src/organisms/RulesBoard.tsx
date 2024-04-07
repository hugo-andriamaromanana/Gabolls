import BoardBackground from '../molecules/BoardBackground';
import RulesText from '../molecules/RulesText';

const RulesBoard = () => {
    return (
        <div className='mt-10'>
            <BoardBackground>
                <RulesText />
            </BoardBackground>

        </div>
    );
};

export default RulesBoard;