from src.rank import rank_games

SAMPLE_GAMES = [
    (1, 11, 26, 30, 48, 53, 54, 60),
    (5, 10, 15, 20, 30, 40, 50, 60),
]


def test_rank_games_when_numbers_empty_numbers():
    games = rank_games(games=SAMPLE_GAMES, drawn_numbers_sv="")
    assert len(games) == len(SAMPLE_GAMES)
    for game in games:
        assert game["score"] == 0


def test_rank_games_when_one_number():
    games = rank_games(games=SAMPLE_GAMES, drawn_numbers_sv="10")
    assert games == [
        {"game": "(5, 10, 15, 20, 30, 40, 50, 60)", "score": 1},
        {"game": "(1, 11, 26, 30, 48, 53, 54, 60)", "score": 0},
    ]


def test_rank_games_when_several_numbers():
    games = rank_games(games=SAMPLE_GAMES, drawn_numbers_sv="1 11 26 30 20 54 60")
    assert games == [
        {"game": "(1, 11, 26, 30, 48, 53, 54, 60)", "score": 6},
        {"game": "(5, 10, 15, 20, 30, 40, 50, 60)", "score": 3},
    ]
