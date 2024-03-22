export interface Scoring {
    player_score: number;
    get(): number;
}


export type PlayerStats = {
    BigPenalties: number;
    SmallPenalties: number;
    Gabos: number;
    BigComebacks: number;
    SmallComebacks: number;
}
