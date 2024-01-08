from dataclasses import dataclass


@dataclass
class fielder_result:
    id: int
    player_id: int
    game_id: int
    times_at_bat: int
    run: int
    hits: int
    k: int
    walks: int
    hit_by_pitch: int
    sacrifice: int
    steal: int
    miss: int
    hr: int
