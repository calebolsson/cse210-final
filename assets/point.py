class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """

    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values. Will convert input text.

        Args:
            x (int): The specified x value.
            y (int): The specified y value.

        Alternative Args:
            x = alph (str): The alphabetical-axis value where 'A' converts to 0
            y = num (str): The numeric-axis value where '1' converts to 0
        """
        if isinstance(x, str) and ord(x) in range(65, 75):
            x = ord(x) - 65
        if isinstance(y, str) and ord(y) in range(48, 58):
            y = ord(y) - 48 - 1
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.

        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.

        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.

        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)

    def get_alph(self):
        return chr(self._x + 65)

    def get_num(self):
        return str(self._y)

    def get_alphnum(self):
        return self.get_alph() + self.get_num()
