class Score():
    def __init__(self):
        self._phase_convert = {"HIT!": "hits", "MISS": "miss", "SUNK": "sunk"}
        self._scores = [{"p": 1, "phase": "--", "hits": 0, "miss": 0, "sunk": 0},
                        {"p": 2, "phase": "--", "hits": 0, "miss": 0, "sunk": 0}]

    def update(self, p, action):
        """Accesses the part of the scoreboard indicated by 'action' and increments it by one.

        Allowed actions:
            hits
            miss
            sunk
        """
        self.set_phase(p, action)
        if action in self._phase_convert:
            self._scores[p][self._phase_convert[action]] += 1
        else:
            self._scores[p][action] += 1

    def reset(self):
        """Runs the ___init___ again to reset the scorecard values."""
        self.__init__()

    def no_victory(self):
        """Returns True while there has yet to be a victor"""
        if self._scores[0]["sunk"] < 5 and self._scores[1]["sunk"] < 5:
            return True
        return False

    def map(self, p):
        """Reads the full score card of one player.

        Args:
            p (int): 0 or 1 index to access the correct player dictionary.

        Returns:
            _scores[p] (dict): All of the data associated with player p's score card.
        """
        return self._scores[p]

    def set_phase(self, p, phase):
        """Updates the phase of the chosen player, and sets the other player's phase to inactive ('--').

        Args:
            p (int): 0 or 1 index to access the correct player dictionary.
            phase (str): the text to save in the active player's phase.
        """
        self._scores[p]["phase"] = phase
        self._scores[(p+1) % 2]["phase"] = "--"
