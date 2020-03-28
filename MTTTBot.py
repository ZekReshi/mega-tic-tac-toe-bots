from abc import ABC, abstractmethod

from Game import Game


class MTTTBot(ABC):

    def __init__(self, game: Game) -> None:
        self.game = game
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def game_over(self, won: bool) -> None:
        pass
