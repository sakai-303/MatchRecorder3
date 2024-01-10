from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Game:
    id: str
    date: date
    day_week: str
    stadium: str
    first_team_id: int
    second_team_id: int
    first_hits: int
    second_hits: int
    first_miss: int
    second_miss: int
    first_point_1: int
    first_point_2: int
    first_point_3: int
    first_point_4: int
    first_point_5: int
    first_point_6: int
    first_point_7: int
    first_point_8: int
    first_point_9: int
    first_point10: int
    first_point11: int
    first_point12: int
    first_point_total: int
    second_point_1: int
    second_point_2: int
    second_point_3: int
    second_point_4: int
    second_point_5: int
    second_point_6: int
    second_point_7: int
    second_point_8: int
    second_point_9: int
    second_point10: int
    second_point11: int
    second_point12: int
    second_point_total: int


@dataclass(frozen=True)
class FielderResult:
    uuid: int
    player_id: str
    game_id: str
    times_at_bat: int
    run: int
    hits: int
    rbi: int
    k: int
    walks: int
    hit_by_pitch: int
    sacrifice: int
    steal: int
    miss: int
    hr: int


@dataclass(frozen=True)
class PitcherResult:
    uuid: str
    player_id: int
    game_id: str
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


@dataclass(frozen=True)
class Bat:
    id: int
    game_id: str
    inning: int
    attacking_team_id: int
    defending_team_id: int
    is_on_base: bool
    rbi: int


@dataclass(frozen=True)
class PitchStats:
    id: int
    id_at_bat: int
    pitcher_id: str
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
    ball_type: str
    speed: int
    pitch_count_at_bat: int
    pitch_count_at_game: int
    ball_result: str
    strike_count: int
    ball_count: int
    top_coordinate: int
    left_coordinate: int
    result_big: str
    result_small: str
    steal: bool


@dataclass(frozen=True)
class Player:
    id: int
    name: str
    team: str
    uniform_number: int
    position: str
    date_of_birth: date
    height: int
    weight: int
    throw_arm: str
    batting_arm: str
    draft_year: int
    draft_rank: str
    total_years: int


@dataclass(frozen=True)
class Team:
    id: int
    name: str


@dataclass(frozen=True)
class ScorePage:
    id: str
    source: str
