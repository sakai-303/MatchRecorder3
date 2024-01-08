import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

root_url = "https://baseball.yahoo.co.jp"

def cache_players():
    team_number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "376"]
    base_url = "https://baseball.yahoo.co.jp/npb/teams"

    for team_number in team_number_list:
        pitcher_page_url = base_url + "/"  + team_number + "/memberlist?kind=p"
        batter_page_url = base_url + "/"  + team_number + "/memberlist?kind=b"

        pitcher_id_list = _get_player_id_list(pitcher_page_url)
        batter_id_list = _get_player_id_list(batter_page_url)
        player_id_list = pitcher_id_list + batter_id_list

        for id in player_id_list:
            base_url = "https://baseball.yahoo.co.jp/npb/player"
            url = base_url + "/" + id + "/top"
            
            cur_dir_path = os.path.dirname(__file__)
            file_path = os.path.join(cur_dir_path, "cache", "player", f"{id}.html")
            _fetch_page(url, file_path)


def _get_player_id_list(url: str) -> list[str]:
    time.sleep(1)
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")

    elements = soup.select("#tm_plyr > tr > td.bb-playerTable__data.bb-playerTable__data--player > a")
    player_link_list = [el.get("href") for el in elements]

    return [link.split("/")[-2] for link in player_link_list]

def cache_games():
    interleague_latest_url = "https://baseball.yahoo.co.jp/npb/schedule/?gameKindIds=26"
    league_latest_url = "https://baseball.yahoo.co.jp/npb/schedule/?gameKindIds=1,2"

    # game_urls = _get_game_urls(interleague_latest_url) + _get_game_urls(league_latest_url)
    game_urls = _get_game_urls(interleague_latest_url)

    for game_url in game_urls:
        game_url = game_url.replace("/index", "")
        game_id = game_url.split("/")[-1]
        game_dir_path = os.path.join(os.path.dirname(__file__), "cache", "game", game_id)
        score_dir_path = os.path.join(game_dir_path, "score")
        
        if os.path.exists(game_dir_path):
            print(f"pass: {game_id}")
            continue

        os.makedirs(game_dir_path)
        os.makedirs(score_dir_path)
        
        _fetch_page(game_url + "/top", os.path.join(game_dir_path, "top.html"))
        _fetch_page(game_url + "/stats", os.path.join(game_dir_path, "stats.html"))
        _fetch_game_score(game_url, score_dir_path)

# ex: https://baseball.yahoo.co.jp/npb/game/2021015004/index
def _get_game_urls(latest_week_url: str) -> list[str]:
    url = latest_week_url
    l = []

    while True:
        time.sleep(1)
        print(f"ページにアクセス: {url}")
        content = requests.get(url).text
        soup = BeautifulSoup(content, "html.parser")

        elements = soup.select("#wk_sche > tbody > tr > td > div > div.bb-scheduleTable__info > p.bb-scheduleTable__status > a")
        l += [el.get("href") for el in elements]

        element = soup.select_one("#wk_nav_h > li:nth-child(1) > a")
        if element is None:
            break
        url = root_url + element.get("href") 
    
    return l
    
def _fetch_game_score(game_url: str, score_dir_path: str):
    url = game_url + "/score?index=0110100"   

    while True:
        time.sleep(1)
        content = requests.get(url).text

        score_id = url[-7:]
        file_path = os.path.join(score_dir_path, f"{score_id}.html")

        components = file_path.split(os.sep)
        cache_index = components.index("cache")
        subpath = os.sep.join(components[cache_index:])
        print(f"ページを取得: {url} → {subpath}")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        soup = BeautifulSoup(content, "html.parser")
        element = soup.select_one("#btn_next")
        if element is None or element.get("href") is None:
            break
        url = root_url + element.get("href")

def _fetch_page(url: str, file_path: str):
    time.sleep(1)
    content = requests.get(url).text
    
    components = file_path.split(os.sep)
    cache_index = components.index("cache")
    subpath = os.sep.join(components[cache_index:])
    print(f"ページを取得: {url} → {subpath}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    cache_games()
