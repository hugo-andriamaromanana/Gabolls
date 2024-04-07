
def _score_gabo(player_score: int) -> ScoringResult:
    return ScoringResult(player_score, ScoringType.Gabo)

def give_gabo(player: Player) -> Player:
    player.scores.append(_score_gabo(player.current_score))
    return player
