import os
from collections.abc import Generator

from entity.entity import ScorePage


def get_game_ids() -> list[str]:
    directory_path = os.path.join(os.path.dirname(__file__), "cache", "game")
    subdirectories = [
        d
        for d in os.listdir(directory_path)
        if os.path.isdir(os.path.join(directory_path, d))
    ]
    return subdirectories


def get_top_page(game_id: str) -> str:
    file_path = os.path.join(
        os.path.dirname(__file__), "cache", "game", game_id, "top.html"
    )
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_stats_page(game_id: str) -> str:
    file_path = os.path.join(
        os.path.dirname(__file__), "cache", "game", game_id, "stats.html"
    )
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_score_page_generator(game_id: str) -> Generator[ScorePage, None, None]:
    directory_path = os.path.join(
        os.path.dirname(__file__), "cache", "game", game_id, "score"
    )
    file_names = os.listdir(directory_path)
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            yield ScorePage(id=file_name[:-5], source=f.read())
