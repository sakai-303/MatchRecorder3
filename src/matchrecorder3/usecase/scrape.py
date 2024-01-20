import datetime
import re
import uuid

from bs4 import BeautifulSoup
from entity.entity import Bat, FielderResult, Game, PitcherResult, PitchStats
from repository.db.repository import (
    add_bat,
    add_fielder_result,
    add_game,
    add_pitch_stats,
    add_pitcher_result,
)
from repository.html.repository import (
    get_game_ids,
    get_score_page_generator,
    get_stats_page,
    get_top_page,
)


def scrape(year: int):
    game_id_list = get_game_ids(year)

    for game_id in game_id_list:
        # TODO: ノーゲームのチェック
        _scrape_game(game_id, year)
        _scrape_fielder_result(game_id, year)


def _scrape_game(game_id: str, year: int):
    top_page_source = get_top_page(game_id)
    soup = BeautifulSoup(top_page_source, "html.parser")

    date_element = soup.select_one("#async-gameCard")
    date_str = date_element.text.split("\n")[1].strip()[:-3]
    dt = datetime.datetime.strptime(date_str, "%m/%d")
    date = datetime.date(year, dt.month, dt.day)
    day_week = date_element.text.split("\n")[1].strip()[-2]

    stadium_element = soup.select_one("#async-gameCard")
    stadium = stadium_element.text.split("\n")[4].strip()

    first_team_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
    )
    first_team_id = first_team_element.get("href").split("/")[-2]

    second_team_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
    )
    second_team_id = second_team_element.get("href").split("/")[-2]

    first_hits_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__total.bb-gameScoreTable__data--hits"
    )
    first_hits = int(first_hits_element.text)

    second_hits_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__total.bb-gameScoreTable__data--hits"
    )
    second_hits = int(second_hits_element.text)

    first_miss_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__total.bb-gameScoreTable__data--loss"
    )
    first_miss = int(first_miss_element.text)

    second_miss_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__total.bb-gameScoreTable__data--loss"
    )
    second_miss = int(second_miss_element.text)

    first_point_1_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(2)"
    )
    first_point_2_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(3)"
    )
    first_point_3_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(4)"
    )
    first_point_4_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(5)"
    )
    first_point_5_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(6)"
    )
    first_point_6_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(7)"
    )
    first_point_7_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(8)"
    )
    first_point_8_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(9)"
    )
    first_point_9_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(10)"
    )
    first_point10_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(11)"
    )
    first_point11_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(12)"
    )
    first_point12_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data:nth-child(13)"
    )

    first_point_1 = (
        int(first_point_1_element.text) if first_point_1_element is not None else None
    )
    first_point_2 = (
        int(first_point_2_element.text) if first_point_2_element is not None else None
    )
    first_point_3 = (
        int(first_point_3_element.text) if first_point_3_element is not None else None
    )
    first_point_4 = (
        int(first_point_4_element.text) if first_point_4_element is not None else None
    )
    first_point_5 = (
        int(first_point_5_element.text) if first_point_5_element is not None else None
    )
    first_point_6 = (
        int(first_point_6_element.text) if first_point_6_element is not None else None
    )
    first_point_7 = (
        int(first_point_7_element.text) if first_point_7_element is not None else None
    )
    first_point_8 = (
        int(first_point_8_element.text) if first_point_8_element is not None else None
    )
    first_point_9 = (
        int(first_point_9_element.text) if first_point_9_element is not None else None
    )
    first_point10 = (
        int(first_point10_element.text) if first_point10_element is not None else None
    )
    first_point11 = (
        int(first_point11_element.text) if first_point11_element is not None else None
    )
    first_point12 = (
        int(first_point12_element.text) if first_point12_element is not None else None
    )

    second_point_1_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(2)"
    )
    second_point_2_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(3)"
    )
    second_point_3_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(4)"
    )
    second_point_4_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(5)"
    )
    second_point_5_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(6)"
    )
    second_point_6_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(7)"
    )
    second_point_7_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(8)"
    )
    second_point_8_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(9)"
    )
    second_point_9_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(10)"
    )
    second_point10_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(11)"
    )
    second_point11_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(12)"
    )
    second_point12_element = soup.select_one(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data:nth-child(13)"
    )

    second_point_1 = (
        int(second_point_1_element.text) if second_point_1_element is not None else None
    )
    second_point_2 = (
        int(second_point_2_element.text) if second_point_2_element is not None else None
    )
    second_point_3 = (
        int(second_point_3_element.text) if second_point_3_element is not None else None
    )
    second_point_4 = (
        int(second_point_4_element.text) if second_point_4_element is not None else None
    )
    second_point_5 = (
        int(second_point_5_element.text) if second_point_5_element is not None else None
    )
    second_point_6 = (
        int(second_point_6_element.text) if second_point_6_element is not None else None
    )
    second_point_7 = (
        int(second_point_7_element.text) if second_point_7_element is not None else None
    )
    second_point_8 = (
        int(second_point_8_element.text) if second_point_8_element is not None else None
    )
    second_point_9 = (
        int(second_point_9_element.text) if second_point_9_element is not None else None
    )
    second_point10 = (
        int(second_point10_element.text) if second_point10_element is not None else None
    )
    second_point11 = (
        int(second_point11_element.text) if second_point11_element is not None else None
    )
    second_point12 = (
        int(second_point12_element.text) if second_point12_element is not None else None
    )

    first_point_total_element = soup.select(
        "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__total"
    )[0]
    first_point_total = int(first_point_total_element.text)

    second_point_total_element = soup.select(
        "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__total"
    )[0]
    second_point_total = int(second_point_total_element.text)

    game = Game(
        id=game_id,
        date=date,
        day_week=day_week,
        stadium=stadium,
        first_team_id=first_team_id,
        second_team_id=second_team_id,
        first_hits=first_hits,
        second_hits=second_hits,
        first_miss=first_miss,
        second_miss=second_miss,
        first_point_1=first_point_1,
        first_point_2=first_point_2,
        first_point_3=first_point_3,
        first_point_4=first_point_4,
        first_point_5=first_point_5,
        first_point_6=first_point_6,
        first_point_7=first_point_7,
        first_point_8=first_point_8,
        first_point_9=first_point_9,
        first_point10=first_point10,
        first_point11=first_point11,
        first_point12=first_point12,
        first_point_total=first_point_total,
        second_point_1=second_point_1,
        second_point_2=second_point_2,
        second_point_3=second_point_3,
        second_point_4=second_point_4,
        second_point_5=second_point_5,
        second_point_6=second_point_6,
        second_point_7=second_point_7,
        second_point_8=second_point_8,
        second_point_9=second_point_9,
        second_point10=second_point10,
        second_point11=second_point11,
        second_point12=second_point12,
        second_point_total=second_point_total,
    )

    add_game(game, year)


def _scrape_fielder_result(game_id: str, year: int):
    stats_page_source = get_stats_page(game_id)
    soup = BeautifulSoup(stats_page_source, "html.parser")

    first_team_player_element_list = soup.select(
        ".bb-blowResultsTable:nth-child(2) > table > tbody > tr"
    )
    second_team_player_element_list = soup.select(
        ".bb-blowResultsTable:nth-child(5) > table > tbody > tr"
    )

    element_list = (
        first_team_player_element_list[:-1] + second_team_player_element_list[:-1]
    )

    l = []
    for player_element in element_list:
        player_name_element = player_element.select_one(
            "td.bb-statsTable__data.bb-statsTable__data--player > a"
        )
        if player_name_element is None:
            player_id = None
        else:
            player_id = player_name_element.get("href").split("/")[-2]

        times_at_bat_element = player_element.select_one("td:nth-child(4)")
        times_at_bat = int(times_at_bat_element.text)

        run_element = player_element.select_one("td:nth-child(5)")
        run = int(run_element.text)

        hits_element = player_element.select_one("td:nth-child(6)")
        hits = int(hits_element.text)

        rbi_element = player_element.select_one("td:nth-child(7)")
        rbi = int(rbi_element.text)

        k_element = player_element.select_one("td:nth-child(8)")
        k = int(k_element.text)

        walks_element = player_element.select_one("td:nth-child(9)")
        walks = int(walks_element.text)

        hit_by_pitch_element = player_element.select_one("td:nth-child(10)")
        hit_by_pitch = int(hit_by_pitch_element.text)

        sacrifice_element = player_element.select_one("td:nth-child(11)")
        sacrifice = int(sacrifice_element.text)

        steal_element = player_element.select_one("td:nth-child(12)")
        steal = int(steal_element.text)

        miss_element = player_element.select_one("td:nth-child(13)")
        miss = int(miss_element.text)

        hr_element = player_element.select_one("td:nth-child(14)")
        hr = int(hr_element.text)

        fielder_result = FielderResult(
            uuid=str(uuid.uuid4()),
            player_id=player_id,
            game_id=game_id,
            times_at_bat=times_at_bat,
            run=run,
            hits=hits,
            rbi=rbi,
            k=k,
            walks=walks,
            hit_by_pitch=hit_by_pitch,
            sacrifice=sacrifice,
            steal=steal,
            miss=miss,
            hr=hr,
        )

        l.append(fielder_result)

    add_fielder_result(l, year)


def _scrape_pitcher_result(game_id: str, year: int):
    stats_page_source = get_stats_page(game_id)
    soup = BeautifulSoup(stats_page_source, "html.parser")

    first_team_player_element_list = soup.select(
        "#gm_stats > section:nth-child(2) > section:nth-child(2) > table > tbody > tr"
    )
    second_team_player_element_list = soup.select(
        "#gm_stats > section:nth-child(2) > section:nth-child(3) > table > tbody > tr"
    )

    element_list = first_team_player_element_list + second_team_player_element_list

    l = []
    for player_element in element_list:
        player_name_element = player_element.select_one(
            "td.bb-scoreTable__data.bb-scoreTable__data--player > a"
        )
        if player_name_element is None:
            player_id = None
        else:
            player_id = player_name_element.get("href").split("/")[-2]

        inning_element = player_element.select_one("td:nth-child(4)")
        inning = float(inning_element.text)

        pitch_num_element = player_element.select_one("td:nth-child(5)")
        pitch_num = int(pitch_num_element.text)

        batter_match_num_element = player_element.select_one("td:nth-child(6)")
        batter_match_num = int(batter_match_num_element.text)

        hits_element = player_element.select_one("td:nth-child(7)")
        hits = int(hits_element.text)

        hr_element = player_element.select_one("td:nth-child(8)")
        hr = int(hr_element.text)

        k_element = player_element.select_one("td:nth-child(9)")
        k = int(k_element.text)

        walks_element = player_element.select_one("td:nth-child(10)")
        walks = int(walks_element.text)

        hit_by_pitch_element = player_element.select_one("td:nth-child(11)")
        hit_by_pitch = int(hit_by_pitch_element.text)

        balks_element = player_element.select_one("td:nth-child(12)")
        balks = int(balks_element.text)

        run_element = player_element.select_one("td:nth-child(13)")
        run = int(run_element.text)

        er_element = player_element.select_one("td:nth-child(14)")
        er = int(er_element.text)

        pitcher_result = PitcherResult(
            uuid=str(uuid.uuid4()),
            player_id=player_id,
            game_id=game_id,
            inning=inning,
            pitch_num=pitch_num,
            batter_match_num=batter_match_num,
            hits=hits,
            hr=hr,
            k=k,
            walks=walks,
            hit_by_pitch=hit_by_pitch,
            balks=balks,
            run=run,
            er=er,
        )

        l.append(pitcher_result)

    add_pitcher_result(l, year)


def _scrape_score_page(game_id: str, year: int):
    score_page_generator = get_score_page_generator(game_id)

    source_page = next(score_page_generator)
    while True:
        try:
            next_page = next(score_page_generator)
        except StopIteration:
            break

        print("Scraping Bat ID: ", score_page.id)
        soup = BeautifulSoup(source_page.source, "html.parser")
        next_soup = BeautifulSoup(next_page.source, "html.parser")

        if soup.select_one("#replay > dt").text == "":
            continue

        _scrape_bat(soup, next_soup, game_id, source_page.id, year)
        _scrape_pitch_stats(soup, next_soup, game_id, source_page.id, year)

        score_page = next_page


def _scrape_bat(
    soup: BeautifulSoup, next_soup: BeautifulSoup, game_id: str, bat_id: str, year: int
):
    if (
        soup.select_one("#replay > dt").text
        == next_soup.select_one("#replay > dt").text
    ):
        return

    inning_element = soup.select_one("#sbo > h4 > em")
    inning = int(inning_element.text[0])

    if inning_element.text[-1] == "表":
        attacking_team_element = soup.select_one(
            "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
        )
        attacking_team_id = int(attacking_team_element.get("href").split("/")[-2])

        defending_team_element = soup.select_one(
            "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
        )
        defending_team_id = int(defending_team_element.get("href").split("/")[-2])

    else:
        attacking_team_element = soup.select_one(
            "#ing_brd > tbody > tr:nth-child(2) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
        )
        attacking_team_id = int(attacking_team_element.get("href").split("/")[-2])

        defending_team_element = soup.select_one(
            "#ing_brd > tbody > tr:nth-child(1) > td.bb-gameScoreTable__data.bb-gameScoreTable__data--team > a"
        )
        defending_team_id = int(defending_team_element.get("href").split("/")[-2])

    result_big_element = soup.select_one("#result > span")

    if result_big_element.get("class") == ["red"]:
        is_on_base = True
    elif "四球" in result_big_element.text:
        is_on_base = True
    elif "死球" in result_big_element.text:
        is_on_base = True
    elif "野選" in result_big_element.text:
        is_on_base = True
    elif "エラー" in result_big_element.text:
        is_on_base = True
    elif "振り逃げ" in result_big_element.text:
        is_on_base = True
    elif "打撃妨害" in result_big_element.text:
        is_on_base = True
    elif "走塁妨害" in result_big_element.text:
        is_on_base = True
    else:
        is_on_base = False

    rbi = int(result_big_element.text).text[-2]

    bat = Bat(
        id=bat_id,
        game_id=game_id,
        inning=inning,
        attacking_team_id=attacking_team_id,
        defending_team_id=defending_team_id,
        is_on_base=is_on_base,
        rbi=rbi,
    )

    add_bat(bat, year)


def _scrape_pitch_stats(
    soup: BeautifulSoup, next_soup: BeautifulSoup, game_id: str, bat_id: str, year: int
):
    if (
        soup.select_one("#replay > dt").text
        == next_soup.select_one("#replay > dt").text
    ):
        _pitch_num_elements = soup.select(
            "#pitchesDetail > section:nth-child(2) > table:nth-child(3) > tbody > tr"
        )
        _pitch_num = len(_pitch_num_elements)
    else:
        _pitch_num = 0

    inning_element = soup.select_one("#sbo > h4 > em")

    if inning_element.text[-1] == "表":
        pitcher_id_element = soup.select_one(
            "#pitcherL > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.nm > a"
        )
        is_pitcher_left_element = soup.select_one(
            "#pitcherL > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.dominantHand"
        )
    else:
        pitcher_id_element = soup.select_one(
            "#pitcherR > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.nm > a"
        )
        is_pitcher_left_element = soup.select_one(
            "#pitcherR > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.dominantHand"
        )

    pitcher_id = pitcher_id_element.get("href").split("/")[-2]
    is_pitcher_left = "左" in is_pitcher_left_element.text

    batter_id_element = soup.select_one(
        "#batt > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.nm > a"
    )
    batter_id = batter_id_element.get("href").split("/")[-2]

    is_batter_left_element = soup.select_one(
        "#batt > tbody > tr > td:nth-child(2) > table > tbody > tr.nm_box > td.dominantHand"
    )
    is_batter_left = "左" in is_batter_left_element.text

    in_box_count_elements = soup.select(
        "#batt > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td > span"
    )
    if in_box_count_elements is None:
        in_box_count = 1
    else:
        in_box_count = len(in_box_count_elements) + 1

    match_count_element = soup.select_one(
        "#pitcherL > div.card.team376 > table > tbody > tr > td:nth-child(2) > table > tbody > tr.score > td:nth-child(2)"
    )
    match_count = int(match_count_element.text)

    if inning_element.text[-1] == "表":
        attacking_team_element = soup.select_one("#gm_mema > table:nth-child(2)")
        defending_table_element = soup.select_one("#gm_memh > table:nth-child(2)")

    else:
        attacking_team_element = soup.select_one("#gm_memh > table:nth-child(2)")
        defending_table_element = soup.select_one("#gm_mema > table:nth-child(2)")

    attack_player_element_list = attacking_team_element.select("tbody > tr")[1:]
    fielder_element_list = defending_table_element.select("tbody > tr")[1:]

    fielder_map = {}
    for fielder_element in fielder_element_list:
        position = fielder_element.select_one("td:nth-child(2)").text
        player_id = (
            fielder_element.select_one("td:nth-child(3) > a").get("href").split("/")[-2]
        )

        fielder_map[position] = player_id

    attack_player_map = {}
    for attack_player_element in attack_player_element_list:
        player_name = attack_player_element.select_one(
            "td:nth-child(3) > a"
        ).text.split(" ")[0]
        player_id = (
            attack_player_element.select_one("td:nth-child(3) > a")
            .get("href")
            .split("/")[-2]
        )

        attack_player_map[player_name] = player_id

    first_runner_element = soup.select_one("#base1 > span")
    second_runner_element = soup.select_one("#base2 > span")
    third_runner_element = soup.select_one("#base3 > span")

    if first_runner_element is None:
        first_runner_id = None
    else:
        first_runner_id = attack_player_map[first_runner_element.text.split(" ")[1]]

    if second_runner_element is None:
        second_runner_id = None
    else:
        second_runner_id = attack_player_map[second_runner_element.text.split(" ")[1]]

    if third_runner_element is None:
        third_runner_id = None
    else:
        third_runner_id = attack_player_map[third_runner_element.text.split(" ")[1]]

    result_big_element = soup.select_one("#result > span")
    result_big = result_big_element.text

    result_small_element = soup.select_one("#result > em")
    result_small = result_small_element.text

    ball_element_list = soup.select(
        "#pitchesDetail > section:nth-child(2) > table:nth-child(3) > tbody > tr"
    )

    strike_count = 0
    ball_count = 0
    for i in range(_pitch_num, len(ball_element_list)):
        ball_element = ball_element_list[i]

        pitch_count_at_game = int(ball_element.select_one("td:nth-child(2)").text)
        ball_type = ball_element.select_one("td:nth-child(3)").text
        speed = int(ball_element.select_one("td:nth-child(4)").text[:-4])
        ball_result = ball_element.select_one("td:nth-child(5)").text

        ball_point_element = soup.select_one(
            f"#pitchesDetail > section:nth-child(2) > table:nth-child(1) > tbody > tr > td > div > span:nth-child({i+1})"
        )
        style_text = ball_point_element.get("style")
        top_text = re.findall(r"top:-?\d+", style_text)[0]
        top_coordinate = int(top_text.replace("top:", ""))
        left_text = re.findall(r"left:-?\d+", style_text)[0]
        left_coordinate = int(left_text.replace("left:", ""))

        result_big: str = None
        result_small: str = None
        is_steal: str = None
        if i == len(ball_element_list) - 1:
            # result取得
            # resultみて盗塁ならsteal=True
            is_last_ball = True

        pitch_stats = PitchStats(
            id=str(uuid.uuid4()),
            id_at_bat=bat_id,
            pitcher_id=pitcher_id,
            is_pitcher_left=is_pitcher_left,
            batter_id=batter_id,
            is_batter_left=is_batter_left,
            in_box_count=in_box_count,
            match_count=match_count,
            c_id=fielder_map["捕"],
            first_id=fielder_map["一"],
            second_id=fielder_map["二"],
            third_id=fielder_map["三"],
            ss_id=fielder_map["遊"],
            lf_id=fielder_map["左"],
            cf_id=fielder_map["中"],
            rf_id=fielder_map["右"],
            first_runner_id=first_runner_id,
            second_runner_id=second_runner_id,
            third_runner_id=third_runner_id,
            ball_type=ball_type,
            speed=speed,
            pitch_count_at_bat=i + 1,
            pitch_count_at_game=pitch_count_at_game,
            ball_result=ball_result,
            strike_count=strike_count,
            ball_count=ball_count,
            top_coordinate=top_coordinate,
            left_coordinate=left_coordinate,
            result_big=result_big,
            result_small=result_small,
            steal=is_steal,
        )

        add_pitch_stats(pitch_stats, year)

        ball_result_type_element = ball_element.select_one("td:nth-child(1) > span")
        type = ball_result_type_element.get("class")[2][-1]

        if type == "1":
            strike_count += 1
        elif type == "2":
            ball_count += 1
