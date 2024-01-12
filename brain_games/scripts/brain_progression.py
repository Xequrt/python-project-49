#!/usr/bin/env python3

from brain_games.body_game.body_game import run_game
from brain_games.games.progression_game import RULES_PROGRESSION, game_data


def main():
    run_game(RULES_PROGRESSION, game_data)


if __name__ == '__main__':
    main()