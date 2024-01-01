from typing import TypedDict


class CheckedGame(TypedDict):
    game: str
    score: int


def _sort_by_correct_numbers(checked_game: CheckedGame) -> int:
    return checked_game["score"]


def rank_games(
    games: list[tuple[int, ...]],
    drawn_numbers_sv: str,
    delimiter: str = " ",
) -> list[CheckedGame]:
    drawn_numbers = {
        int(n.strip()) for n in drawn_numbers_sv.split(delimiter) if len(n.strip())
    }
    scores = []
    for game in games:
        scores.append(sum([n in drawn_numbers for n in game]))

    result = [
        CheckedGame(game=str(game), score=score)
        for game, score in zip(games, scores, strict=True)
    ]
    result = sorted(result, key=_sort_by_correct_numbers, reverse=True)
    return result
