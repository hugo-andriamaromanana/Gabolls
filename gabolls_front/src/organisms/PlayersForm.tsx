import { useEffect, useState } from 'react';
import DefaultButton from '../atoms/Buttons/DefaultButton';
import DefaultInput from '../atoms/DefaultInput';

const PLAYERS_STORAGE_KEY = 'COUNT_PLAYERS';

const MAX_PLAYERS = 6;
const MIN_PLAYERS = 3;

type Player = {
    id: string;
    name: string;
};

const PlayersForm = () => {
    const [players, setPlayers] = useState<Player[]>([]);

    useEffect(() => {
        const storagePlayers = JSON.parse(
            localStorage.getItem(PLAYERS_STORAGE_KEY) || '[]'
        );
        if (storagePlayers.length) {
            setPlayers(storagePlayers);
        } else {
            setPlayers([
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
            ]);
        }
    }, []);

    useEffect(() => {
        localStorage.setItem(PLAYERS_STORAGE_KEY, JSON.stringify(players));
    }, [players]);

    const addPlayer = () => {
        if (players.length >= MAX_PLAYERS) return;

        const newId = players.length + 1;
        setPlayers([
            ...players,
            { id: newId.toString(), name: `Player ${newId}` }
        ]);
    };

    const handleChange = (name: string, index: number) => {
        const newPlayers = [...players];
        newPlayers[index].name = name;
        setPlayers(newPlayers);
    };

    return (
        <div className='flex flex-col w-full md:w-2/3 items-center'>
            {players?.map(player => (
                <div key={player.id} className='group/input my-1 flex flex-row'>
                    <DefaultInput
                        key={player.id}
                        placeholder={player.name}
                        onChange={e =>
                            handleChange(
                                e.target.value,
                                players.indexOf(player)
                            )
                        }
                    />
                    {players.indexOf(player) >= MIN_PLAYERS && (
                        <div className='group/delete invisible w-0 group-hover/input:visible group-hover/input:w-3/12'>
                            <DefaultButton
                                title='X'
                                className='bg-gradient-to-r from-primary to-secondary w-fit'
                                onClick={() =>
                                    setPlayers(
                                        players.filter(p => p.id !== player.id)
                                    )
                                }
                            />
                        </div>
                    )}
                </div>
            ))}
            {players.length < MAX_PLAYERS && (
                <DefaultButton
                    title='+'
                    className='bg-gradient-to-r from-primary to-secondary w-fit mt-2'
                    onClick={addPlayer}
                />
            )}
        </div>
    );
};

export default PlayersForm;
