from abc import ABC, abstractmethod

from Game import Game


class MTTTBot(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def play(self, game: Game):
        pass

    @abstractmethod
    def game_over(self, game: Game, won: bool) -> None:
        pass
