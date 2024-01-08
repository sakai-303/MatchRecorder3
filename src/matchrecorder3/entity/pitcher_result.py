from dataclasses import dataclass


@dataclass
class pitcher_result:
    id: int
    player_id: int
    game_id: int
    inning: float
    pitch_num: int
    batter_match_num: int
    hits: int
    hr: int
    k: int
    walks: int
    hit_by_pitch: int
    balks: int
    run: int
    er: int
