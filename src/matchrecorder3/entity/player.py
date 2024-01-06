import datetime
from dataclasses import dataclass


@dataclass
class Player:
    id: int
    name: str
    team: str
    uniform_number: int
    position: str
    date_of_birth: datetime
    height: int
    weight: int
    throw_arm: str
    batting_arm: str
    draft_year: int
    draft_rank: str
    total_years: int
