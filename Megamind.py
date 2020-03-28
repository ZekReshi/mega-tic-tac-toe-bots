import numpy as np

from typing import Dict, List, Tuple

from Game import Game, State
from MTTTBot import MTTTBot


class Megamind(MTTTBot):

    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self.mind: Dict[State, np.ndarray] = {}
        self.decisions: Dict[State, Tuple[int, int, int, int]] = List[]

    def play(self):
        if self.game.game_over():
            return
        if self.game.state not in self.mind:
            self.mind[self.game.state] = np.zeros((3, 3, 3, 3))
        while True:
            # calc probs and pick position
            position = (0, 0, 0, 0)
            if self.game.play(position):
                self.decisions[self.game.state] = position
                break
            self.mind[self.game.state][position] = None

    def game_over(self, won: bool) -> None:
        for state, position in self.decisions.items():
            # reward or punish
            pass
