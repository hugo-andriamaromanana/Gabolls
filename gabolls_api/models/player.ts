// Player
import { Card } from "./deck";


export type PlayerStats = {
    BigPenalties: number;
    SmallPenalties: number;
    Gabos: number;
    BigComebacks: number;
    SmallComebacks: number;
}

export type Player = {
    id: string;
    name: string;
    hand: Card[];
    score: number;
    stats: PlayerStats;
}


export class Gamer {
    score: number = 0;
}