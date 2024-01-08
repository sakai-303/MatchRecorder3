import datetime
from dataclasses import dataclass

@dataclass
class Bat:
    id: int
    game_id: int
    inning: int
    attacking_team: str
    deffanding_team: str
    is_out: bool
    rbi: int
    result_big: str
    result_small: str
    is_terminated_by_runner_out: bool
