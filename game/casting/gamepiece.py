from assets.color import Color


class Gamepiece():
    """A part of the game that can be represented on the game board."""

    def __init__(self, text="", r=0, g=0, b=0, a=255):
        """Constructs a new piece that is represented by a symbol and a color."""
        self._text = text
        self._color = Color(r, g, b, a)

    def set_color(self, r, g, b, a):
        """Changes the color of the object."""
        self._color = Color(r, g, b, a)

    def set_text(self, text):
        """Changes the text of the object."""
        self._text = text

    def get_token(self):
        """ERROR: This method has not yet been defined for this class."""
        print("ERROR: This method has not yet been defined for this class.")
        return -1
