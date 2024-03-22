import { Scoring } from "./score";


export class GaboScoring implements Scoring {
    constructor(public player_score: number) {}

    get(): number {
        return this.player_score;
    }
}
