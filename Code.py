from games import games_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "movie" (a tuple)
def get_score(game: Tuple[str, str, str, int, List[str]]) -> str:
    return game[0]

def get_winner(game: Tuple[str, str, str, int, List[str]]) -> str:
    return game[1]

def get_loser(game: Tuple[str, str, str, int, List[str]]) -> str:
    return game[2]

def get_year(game: Tuple[str, str, str, int, List[str]]) -> int:
    return game[3]


def get_captains(game: Tuple[str, str, str, int, List[str]]) -> List[str]:
    return game[4]