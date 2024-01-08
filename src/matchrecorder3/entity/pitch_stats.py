from dataclasses import dataclass


@dataclass
class PitchStats:
    id: int
    id_at_bat: int
    pitcher_id: int
    is_pitcher_left: bool
    batter_id: int
    is_batter_left: bool
    in_box_count: int
    match_count: int
    c_id: int
    first_id: int
    second_id: int
    third_id: int
    ss_id: int
    lf_id: int
    cf_id: int
    rf_id: int
    first_runner_id: int
    second_runner_id: int
    third_runner_id: int
    pitch_count_at_bat: int
    pitch_count_at_game: int
    ball_type: str
    speed: int
    ball_result: str
    strike_count: int
    ball_count: int
    top_coordinate: int
    left_coordinate: int
    steal: bool
    steal_non_pitch: bool
