import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def fetch_player():
    team_number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "376"]
    base_url = "https://baseball.yahoo.co.jp/npb/teams"

    for team_number in team_number_list:
        pitcher_page_url = base_url + "/"  + team_number + "/memberlist?kind=p"
        batter_page_url = base_url + "/"  + team_number + "/memberlist?kind=b"

        pitcher_id_list = _get_player_id_list(pitcher_page_url)
        batter_id_list = _get_player_id_list(batter_page_url)
        player_id_list = pitcher_id_list + batter_id_list

        for id in player_id_list:
            _fetch_player_page(id)


def _get_player_id_list(url: str) -> list[str]:
    time.sleep(1)
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")

    player_link_list = [
        el.get("href")
        for el in soup.select(
            "#tm_plyr > tr > td.bb-playerTable__data.bb-playerTable__data--player > a"
        )
    ]

    return [link.split("/")[-2] for link in player_link_list]


def _fetch_player_page(id: str):
    base_url = "https://baseball.yahoo.co.jp/npb/player"
    url = base_url + "/" + id + "/top"

    time.sleep(1)
    content = requests.get(url).text

    cur_dir_path = os.path.dirname(__file__)
    file_path = os.path.join(cur_dir_path, "cache", "player", f"{id}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    fetch_player()