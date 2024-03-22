// Player
import { Card } from "./deck";

export type Player = {
    id: string;
    name: string;
    hand: Card[];
    score: number;
}

export class Gamer {
    score: number = 0;
}
















































