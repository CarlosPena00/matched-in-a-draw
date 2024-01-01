import pandas as pd
import streamlit as st

from src.rank import rank_games

# TODO: Change `CHOSEN_GAMES` to be an user input
CHOSEN_GAMES = [
    (1, 11, 26, 30, 48, 53, 54, 60),
    (5, 10, 15, 20, 30, 40, 50, 60),
    # ...
]


def main():
    st.title("Boa sorte!")
    user_input = st.text_input("Digite os números sorteados separados por espaço.")
    user_input = user_input.strip()

    if user_input:
        numbers = {int(num.strip()) for num in user_input.split(" ") if len(num)}
        st.write(f"Números Sorteados: {numbers}")
        games = rank_games(
            games=CHOSEN_GAMES, drawn_numbers_sv=user_input, delimiter=" "
        )
        df = pd.DataFrame(games).rename(
            columns={"game": "Jogo", "score": "Números sorteados"}
        )
        st.dataframe(df)


if __name__ == "__main__":
    main()
