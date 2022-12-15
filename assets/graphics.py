from assets.color import Color


GRID = {
    "legend": "      1     2     3     4     5     6     7     8     9    10",
    "top": "   ╔═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╗",
    "cells": " {0} ║  {1}  │  {2}  │  {3}  │  {4}  │  {5}  │  {6}  │  {7}  │  {8}  │  {9}  │  {10}  ║",
    "wall": "   ╟─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────╢",
    "bottom": "   ╚═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╝"
}

SCORE = [
    "",
    "      ╔════════════╗",
    "      ║  Player {p}  ║",
    "      ║{phase:^12}║",
    "      ║  Hits:{hits:3}  ║",
    "      ║  Miss:{miss:3}  ║",
    "      ║  Sunk:  {sunk}  ║",
    "      ╚════════════╝"
]

ERROR = {
    "blank_input": "Error: Empty input",
    "position_syntax": "Error: Syntax (example input: C4)",
    "direction_syntax": "Error: Syntax (example input: north)",
    "out_of_board": "Error: Ship {} is not all on the board"
}

PROMPT = {
    "position": "Place Ship {} (length {}): ",
    "direction": "Which direction will the ship face?\nType a direction (north, south, east, west): ",
    "FIRE": "P{} input target coordinates: "
}
