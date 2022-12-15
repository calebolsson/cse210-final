from game.casting.gamepiece import Gamepiece
from assets.point import Point


class Ship(Gamepiece):
    """A maritime vessel, in this case part of a wartime fleet.

    Attributes:
        _len (int): the length the ship will extend from _head, either [2,3,3,4,5]
        _head (Point): the location on the board of the beginning of the ship
        _vector (Point): the direction away from _head that the ship points as a unit vector
        _segments (list (Point)): all the map locations the ship fills, iterable
        _hits (int): counts the number of hits this ship has taken
        _sunk (bool): if the ship has been hit enough to be sunk
    """

    def __init__(self, len, pos, vector_str):
        """Creates a new Ship. A ship has a head and a length so that each of its segments is indexable.

        Args:
            len (int): the length the ship will extend from _head, choose from [2,3,3,4,5]
            pos (str): the letter-number location of the ship's head, used to make _head
            vector_str (str): the direction the ship will extend from _head
        """
        super().__init__()
        self._len = len
        self._head = Point(pos[0], pos[1])
        vector_map = {'N': Point(-1, 0), 'S': Point(1, 0),
                      'W': Point(0, -1), 'E': Point(0, 1)}
        self._vector = vector_map[vector_str]
        self._segments = [self._head]
        for l in range(len - 1):
            self._segments.append(self._segments[-1].add(self._vector))
        self._hits = 0
        self._sunk = False

    def self_validate(self):
        for this_segment in self._segments:
            if (this_segment.get_x() < 0) or (this_segment.get_y() < 0):
                return False
        return True

    def is_sunk(self):
        """Checks if the ship has been sunk yet.

        Returns:
            _sunk (bool)
        """
        return self._sunk

    def is_hit(self, target_cell):
        """Checks to see if the target is found from among the segments of the ship. If it is hit, it will also update the 'sunk' status if it changes. The bool returned only indicates if there was a hit.

        Args:
            target (str): the letter-number position of the target cell on the board

        Returns:
            bool
        """
        for segment in self._segments:
            if segment.equals(target_cell):
                self._hits += 1
                if self._hits == self._len:
                    self._sunk = True
                return True
        return False

    def get_token(self):
        display = "["
        for i in range(len(self._segments)):
            display += self._segments[i].get_alphnum() + ","
        return display[:-1] + "]"
