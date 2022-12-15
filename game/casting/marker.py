from game.casting.gamepiece import Gamepiece


class Marker(Gamepiece):
    """A hit/miss token.
    
    Attributes:
        _text (str): how to display the marker
        _color (Color): the color of the marker
    """
    def __init__(self, text=" ", r=0, g=0, b=0, a=255):
        """Creates a new hit/miss marker.
        
        Args:
            text (str): how to display the marker
            r (int): part of a Color(), an int between 0 and 255
            g (int): part of a Color(), an int between 0 and 255
            b (int): part of a Color(), an int between 0 and 255
            a (int): part of a Color(), an int between 0 and 255
        """
        super().__init__(text, r, g, b, a)

    def hit(self):
        """Sets the marker as a 'hit' marker"""
        self.set_text("X")
        self.set_color(255, 0, 0, 255)
        return "HIT!"

    def miss(self):
        """Sets the marker as a 'miss' marker"""
        self.set_text("O")
        self.set_color(255, 255, 255, 255)
        return "MISS"

    def get_token(self):
        return self._text

    