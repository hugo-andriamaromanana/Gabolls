import { RouteObject } from 'react-router-dom';

import Home from './pages/count/Home';
import Error404 from './pages/errors/Error404';
import PlayerSelection from './pages/count/PlayerSelection';
import Scores from './pages/count/Scores';
import PointsEntry from './pages/count/PointsEntry';
import Game from './pages/game/Game';
import Rules from './pages/Rules';
import GameSelection from './pages/count/GameSelection';

const routes: RouteObject[] = [
    {
        path: '/',
        element: <Home />,
        errorElement: <Error404 />
    },
    {
        path: '/rules',
        element: <Rules />
    },
    {
        path: '/count',
        element: <GameSelection />
    },
    {
        path: '/count/players',
        element: <PlayerSelection />
    },
    {
        path: '/count/scores',
        element: <Scores />
    },
    {
        path: '/count/player/:id',
        element: <PointsEntry />
    },
    {
        path: '/play',
        element: <Game />
    }
];

export default routes;
