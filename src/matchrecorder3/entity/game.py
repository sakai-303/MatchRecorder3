from dataclasses import dataclass
from datetime import date


@dataclass
class GameData:
    id: int
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
