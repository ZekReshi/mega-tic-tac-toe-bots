from abc import ABC, abstractmethod
from typing import Tuple

from Game import State


class MTTTBot(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def play(self, state: State) -> Tuple[int, int, int, int]:
        pass
