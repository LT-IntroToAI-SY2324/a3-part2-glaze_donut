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

def _by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    results = []
    # print(matches)
    for game in games_db:
        if int(matches[0]) == get_year(game):
            # print(get_title(movie))
            results.append(get_title(movie))
    # print(results)
    return results

a_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"), title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"), title_before_year),
    (str.split("what movies were made after _"), title_after_year),
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("% appeared in what movies"), title_by_actor),
    (str.split("in what movies did % appear"), title_by_actor),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            # print(answer)
            return answer if answer else ["No answers"]   
    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
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