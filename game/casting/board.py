import os
from game.casting.marker import Marker
from game.casting.ship import Ship
from assets.point import Point
from assets.graphics import GRID, SCORE, ERROR, PROMPT


class Gameboard():
    def __init__(self):
        self._ships = [[], []]  # this will hold the ship data for both players
        self._cell = []  # this will be a 3D array that will store each player's hit/miss board
        for alph in range(10):
            self._cell.append([])
            for num in range(10):
                self._cell[alph].append([Marker(), Marker()])
                # self._cell[alph].append([chr(65 + alph), " "]) # DEBUG

    def is_blank(self, input):
        """Checks if an input has 0 or less characters in it's string form.

        Args:
            input: will be converted into a str before checking its length

        Returns:
            bool: returns True if the length was 0 or less"""
        if len(str(input)) <= 0:
            return True
        else:
            return False

    def validate_point(self, pos):
        """Returns true if the point is valid, returns false if it needs to print an error message"""
        if self.is_blank(pos) or len(pos) < 2:
            print(ERROR["blank_input"])
            return False
        elif not (ord(pos[0]) in range(65, 75)) or not (ord(pos[1]) in range(48, 58)):
            print(ERROR["position_syntax"])
            return False
        else:
            return True

    def validate_direction(self, angle):
        """Returns true if the direction is valid, returns false if it needs to print an error message"""
        if self.is_blank(angle):
            print(ERROR["blank_input"])
            return False
        elif not (angle[0] in ["n", "s", "w", "e", "N", "S", "W", "E"]):
            print(ERROR["direction_syntax"])
            return False
        else:
            return True

    def add_ship(self, p, nth_ship, len):
        """Acts as input validation before adding a ship to the selected player's collection of ships.

        Args:
            p (int): player who the ship belongs to
            len (int): length of the ship, choose from [2,3,3,4,5]
            pos (str): the player-input location to place the ship's head (format 'letter-number')
            vector_str (str): the cardinal direction the ship will extend from 'pos'

        Returns:
            bool: if the add failed, add_ship will return True
        """
        try_again = True
        while try_again:
            try_again_inner = [True, True]
            while try_again_inner[0]:
                pos = input(PROMPT["position"].format(nth_ship, len))
                if self.validate_point(pos):
                    try_again_inner[0] = False
            while try_again_inner[1]:
                angle = input(PROMPT["direction"])
                if self.validate_direction(angle):
                    try_again_inner[1] = False
                    angle = angle[0].capitalize()
            ship = Ship(len, pos, angle)
            if ship.self_validate():
                try_again = False
                self._ships[p].append(ship)
            else:
                print(ERROR["out_of_board"].format(ship.get_token()))
            

    def print_board(self, p, score):
        os.system('cls')
        b = 0
        box = ""
        for row in range(22):
            if row >= 4 and row < 11:
                b += 1
                box = SCORE[b % len(SCORE)].format_map(score.map(p % 2))
            elif row >= 11 and row <= 18:
                b += 1
                box = SCORE[b % len(SCORE)].format_map(score.map((p + 1) % 2))
            else:
                box = ""
            if row == 0:
                print(GRID["legend"])
            elif row == 1:
                print(GRID["top"])
            elif row == 21:
                print(GRID["bottom"])
            elif row % 2:
                print(GRID["wall"] + box)
            else:
                i = int((row - 1) / 2)
                print(GRID["cells"].format(chr(65 + i), self._cell[i][0][p].get_token(), self._cell[i][1][p].get_token(), self._cell[i][2][p].get_token(), self._cell[i][3][p].get_token(), self._cell[i][4][p].get_token(
                ), self._cell[i][5][p].get_token(), self._cell[i][6][p].get_token(), self._cell[i][7][p].get_token(), self._cell[i][8][p].get_token(), self._cell[i][9][p].get_token()) + box)

    def show_ships(self, p):
        ships = len(self._ships[p])
        if ships >= 0:
            for i in range(ships):
                print("Ship {}: {}".format(
                    i + 1, self._ships[p][i].get_token()))

    def target(self, this_player, other_player):
        """Returns the status of the shot
        
        Possible return values:
            MISS
            HIT!
            SUNK
        """
        while True:
            target = input(PROMPT["FIRE"].format(this_player + 1))
            if self.validate_point(target):
                break
        target_cell = Point(target[0], target[1])
        for ship in self._ships[other_player]:
            if ship.is_hit(target_cell):
                if ship.is_sunk():
                    self._cell[target_cell.get_x()][target_cell.get_y()][this_player].hit()
                    return "SUNK"
                return self._cell[target_cell.get_x()][target_cell.get_y()][this_player].hit()
        return self._cell[target_cell.get_x()][target_cell.get_y()][this_player].miss()