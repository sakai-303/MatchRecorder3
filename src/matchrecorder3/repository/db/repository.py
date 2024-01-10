from entity.entity import Bat, FielderResult, Game, PitcherResult, PitchStats


def add_game(game: Game, year: int):
    # TODO: 既にDBにレコードがある場合はスキップする
    print(game)
    pass


def add_fielder_result(fielder_result_list: list[FielderResult], year: int):
    print(fielder_result_list)


def add_pitcher_result(pitcher_result_list: list[PitcherResult], year: int):
    for pitcher_result in pitcher_result_list:
        print(pitcher_result.game_id)


def add_bat(bat_list: list[Bat], year: int):
    print(bat_list)


def add_pitch_stats(pitch_stats_list: list[PitchStats], year: int):
    print(pitch_stats_list)
