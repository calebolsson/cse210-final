import os
from game.casting.board import Gameboard
from game.casting.score import Score


class Director():
    def __init__(self):
        self._is_playing = True
        self._board = Gameboard()
        self._score = Score()
        self._p = 0

    def this_player(self):
        return (self._p + 1)

    def _p_next(self):
        return (self.this_player() % 2)

    def next_player(self):
        return self._p_next() + 1

    def next_turn(self, phase="--"):
        self._score.set_phase(self._p, phase)
        self._board.print_board(self._p, self._score)
        if phase == "HIT!" or phase == "SUNK":
            input("P{} hit a ship! Press enter to go again".format(
                self.this_player()))
        else:
            input("[P{}: PRESS ENTER AND PASS TO P{}]".format(
                self.this_player(), self.next_player()))
            self._p = self._p_next()
        os.system('cls')

    def start_game(self):
        self._board.print_board(self._p, self._score)
        input("[PRESS ENTER TO PLAY]")
        os.system('cls')
        for p in [0, 1]:
            input("[P{}: PRESS ENTER TO PLACE SHIPS]".format(self.this_player()))
            ship_lengths = [5, 4, 3, 3, 2]
            for ship in range(len(ship_lengths)):
                self._score.set_phase(
                    self._p, "SHIPS: {}/{}".format(ship + 1, 5))
                self._board.print_board(self._p, self._score)
                self._board.show_ships(self._p)
                self._board.add_ship(self._p, ship + 1, ship_lengths[ship])
            self.next_turn()
        while self._score.no_victory():
            self._score.set_phase(self._p, "FIRE")
            self._board.print_board(self._p, self._score)
            mark_result = self._board.target(self._p, self._p_next())
            self._score.update(self._p, mark_result)
            self.next_turn(mark_result)
        print("Player {} sunk 5 ships!".format(self._p))
