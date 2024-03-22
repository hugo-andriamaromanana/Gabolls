import { PointScoring } from "./pointScoring";
import { PenaltyScoring, PenaltyType } from "./penaltyScoring";
import { Gamer } from "../models/player";
import { GaboScoring } from "./gaboScoring";


export function testScore() {
    let player = new Gamer();
    player.score = new PointScoring(10, player.score).get();
    player.score = new PointScoring(10, player.score).get();
    console.log(player.score);
    player.score = new PenaltyScoring(PenaltyType.Big, player.score).get();
    console.log(player.score);
    player.score = new PointScoring(30, player.score).get();
    console.log(player.score);
    player.score = new GaboScoring(player.score).get();
    console.log(player.score)
}
