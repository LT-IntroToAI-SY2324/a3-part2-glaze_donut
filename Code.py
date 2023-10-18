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

def winner_by_year(matches: List[str]) -> List[str]:
    results = []
    
    for game in games_db:
        if int(matches[0]) == get_year(game):
            
            results.append(get_winner(game))
    
    return results
def loser_by_year(matches: List[str]) -> List[str]:
    results = []
    
    for game in games_db:
        if int(matches[0]) == get_year(game):
            
            results.append(get_loser(game))
   
    return results
def teams_by_year(matches: List[str]) -> List[str]:
    results = []
    
    for game in games_db:
        if int(matches[0]) == get_year(game):
            
            results.append(get_loser(game))
            results.append(get_winner(game))
    
    return results
def captains_by_year(matches: List[str]) -> List[str]:
    results = []
   
    for game in games_db:
        if int(matches[0]) == get_year(game):
            
            results=(get_captains(game))
    
    return results
def points_by_year(matches: List[str]) -> List[str]:
    results = []
    
    for game in games_db:
        if int(matches[0]) == get_year(game):
            
            results.append(get_score(game))
    
    return results
def years_by_team(matches: List[str]) -> List[str]:
    results = []
    
    for game in games_db:
        if int(matches[0]) == get_winner(game):
            
            results.append(get_year(game))
        if int(matches[0]) == get_loser(game):
            
            results.append(get_year(game))
    
    return results
def years_by_captain(matches: List[str]) -> List[str]:
    results = []
    for game in games_db:
        if matches[0] in get_captains(game):
            results.append(get_year(game))
    
    return results
def numwins_by_team(matches: List[str]) -> List[str]:
    count = 0
    
    for game in games_db:
        if int(matches[0]) == get_winner(game):
           count+=1

    return count
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("Who were the team captains in _"), captains_by_year),
    (str.split("What was the final score in _"), points_by_year),
    (str.split("What world cups has _ played in"), years_by_team),
    (str.split("Who won in _"), winner_by_year),
    (str.split("Who lost in _"), loser_by_year),
    (str.split("What year has the captain _ played in"), years_by_captain),
    (str.split("What team lost and what team won in _"), teams_by_year),
    (str.split("How many times has _ won"), numwins_by_team),
]


def search_pa_list(src: List[str]) -> List[str]:
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            
            return answer if answer else ["No answers"]   
    return ["I don't understand"]


def query_loop() -> None:
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")