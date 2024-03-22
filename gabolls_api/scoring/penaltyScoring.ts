import {Scoring} from "./score"

const SMALL_PENALTY = 25;
const BIG_PENALTY = 50;

export enum PenaltyType  {
    Small = "Small",
    Big = "Big"
}

export const PENALTY_SCORES: { [key in PenaltyType]: number } = {
    [PenaltyType.Small]: SMALL_PENALTY,
    [PenaltyType.Big]: BIG_PENALTY
};


export class PenaltyScoring implements Scoring {
    constructor(private penaltyType: PenaltyType, public player_score: number) {}

    get(): number {
        return this.player_score + PENALTY_SCORES[this.penaltyType];
    }
    stats()
}
