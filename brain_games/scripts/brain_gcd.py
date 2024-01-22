#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.gcd_game import RULES_GCD, get_game_data


def main():
    run_game(RULES_GCD, get_game_data)


if __name__ == '__main__':
    main()
