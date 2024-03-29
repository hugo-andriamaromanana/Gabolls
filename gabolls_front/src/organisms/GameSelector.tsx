import { useEffect, useState } from 'react';
import DefaultButton from '../atoms/Buttons/DefaultButton';
import { Player } from './PlayersForm';

type Game = {
    id: string;
    name: string;
    players: Player[];
};

const GameSelector = () => {
    const [games, setGames] = useState<Game[]>([]);

    useEffect(() => {
        setGames([
            {
                id: '1',
                name: 'Game 1',
                players: [
                    {
                        id: '1',
                        name: 'Player 1'
                    },
                    {
                        id: '2',
                        name: 'Player 2'
                    },
                    {
                        id: '3',
                        name: 'Player 3'
                    },
                    {
                        id: '4',
                        name: 'Player 4'
                    },
                    {
                        id: '5',
                        name: 'Player 5'
                    },
                    {
                        id: '6',
                        name: 'Player 6'
                    }
                ]
            },
            {
                id: '2',
                name: 'Game 2',
                players: [
                    {
                        id: '1',
                        name: 'Player 1'
                    },
                    {
                        id: '2',
                        name: 'Player 2'
                    },
                    {
                        id: '3',
                        name: 'Player 3'
                    }
                ]
            },
            {
                id: '3',
                name: 'Game 3',
                players: [
                    {
                        id: '1',
                        name: 'Player 1'
                    },
                    {
                        id: '2',
                        name: 'Player 2'
                    },
                    {
                        id: '3',
                        name: 'Player 3'
                    }
                ]
            },
            {
                id: '5',
                name: 'Game 5',
                players: [
                    {
                        id: '1',
                        name: 'Player 1'
                    },
                    {
                        id: '2',
                        name: 'Player 2'
                    },
                    {
                        id: '3',
                        name: 'Player 3'
                    }
                ]
            },
            {
                id: '4',
                name: 'Game 4',
                players: [
                    {
                        id: '1',
                        name: 'Player 1'
                    },
                    {
                        id: '2',
                        name: 'Player 2'
                    },
                    {
                        id: '3',
                        name: 'Player 3'
                    }
                ]
            }
        ]);
    }, []);

    const gamePlayersName = (players: Player[]) => {
        return players.map(player => player.name).join(', ');
    };

    return (
        <div className='flex flex-col w-screen md:w-2/3 items-center overflow-hidden'>
            <div>Recent games</div>
            {games?.map(game => (
                <DefaultButton
                    key={game.id}
                    title={game.name}
                    className='text-sm w-full shadow-sm md:shadow-lg hover:scale-100 sm:hover:scale-110 max-w-xs my-1 md:my-2 md:h-20'
                >
                    <div className='text-gray-400 w-full overflow-hidden whitespace-nowrap overflow-ellipsis md:overflow-visible md:whitespace-normal'>
                        {gamePlayersName(game.players)}
                    </div>
                </DefaultButton>
            ))}
        </div>
    );
};

export default GameSelector;
