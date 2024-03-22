import {Scoring} from './score'

const SMALL_COMEBACK_TRIGGER = 50;
const SMALL_COMEBACK_SCORING = 25;
const BIG_COMEBACK_TRIGGER = 100;
const BIG_COMEBACK_SCORING = 50;

const COMEBACKS: { [key: number]: number } = {
    [SMALL_COMEBACK_TRIGGER]: SMALL_COMEBACK_SCORING,
    [BIG_COMEBACK_TRIGGER]: BIG_COMEBACK_SCORING
};

export class PointScoring implements Scoring {
    constructor(private points: number, public player_score: number) {}

    private updateScoreWithComebacks(): number {
        if (this.points in COMEBACKS) {
            return COMEBACKS[this.points];
        }
        return this.points;
    }

    get(): number {
        this.points = this.player_score + this.points;
        return this.updateScoreWithComebacks();
    }
}