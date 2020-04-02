from typing import Tuple, List

import numpy as np


class State:

    def __init__(self,
                 board: np.ndarray = None,
                 cell: Tuple[int, int] = None) -> None:
        self.board = board if board is not None else np.full((3, 3, 3, 3), 0)
        self.cell = cell
        self.turn: bool = self.board.sum() == 0

    def print(self) -> None:
        output: List[str] = []
        for i_index, i in enumerate(self.board):
            for j_index, j in enumerate(i):
                for k_index, k in enumerate(j):
                    for l_index, l in enumerate(k):
                        if j_index == 0 and l_index == 0:
                            output.append("")
                        if l_index != 0:
                            output[i_index * 4 + k_index] += " "
                        if j_index != 0 and l_index == 0:
                            output[i_index * 4 + k_index] += "|"
                        output[i_index * 4 + k_index] += " " if l == 0 else "X" if l == 1 else "O"
            if i_index != 2:
                output.append("-----------------")
        for output_str in output:
            print(output_str)


class Game:

    def __init__(self) -> None:
        self.state = State()
        self.history = List[State]

    def play(self, position: Tuple[int, int, int, int]) -> bool:
        for coordinate in position:
            if coordinate < 0 or coordinate > 2 or self.state.board[position] != 0 or \
                    self.cell_over(self.state.board[position[:2]]) or \
                    (self.state.cell is not None and self.state.cell != position[:2]):
                return False
        self.state.board[position] = 1 if self.state.turn else -1
        self.state.cell = None if self.cell_over(self.state.board[position[2:]]) else position[2:]
        self.state.turn = not self.state.turn
        self.history.add(self.state)
        return True

    def cell_over(self, cell: np.ndarray) -> bool:
        return self.cell_winner(cell) != 0

    @staticmethod
    def cell_winner(cell: np.ndarray) -> int:
        if cell[1, 1] != 0 and (
                cell[1, 1] == cell[0, 0] and cell[1, 1] == cell[2, 2] or  # top left to bottom right
                cell[1, 1] == cell[0, 1] and cell[1, 1] == cell[2, 1] or  # top to bottom
                cell[1, 1] == cell[0, 2] and cell[1, 1] == cell[2, 0] or  # top right to bottom left
                cell[1, 1] == cell[1, 0] and cell[1, 1] == cell[1, 2]  # left to right
        ):
            return cell[1, 1]
        if cell[0, 0] != 0 and (
                cell[0, 0] == cell[1, 0] and cell[0, 0] == cell[2, 0] or  # top left to bottom left
                cell[0, 0] == cell[0, 1] and cell[0, 0] == cell[0, 2]  # top left to top right
        ):
            return cell[0, 0]
        if cell[2, 2] != 0 and (
                cell[2, 2] == cell[1, 2] and cell[2, 2] == cell[0, 2] or  # bottom right to top right
                cell[2, 2] == cell[2, 1] and cell[2, 2] == cell[2, 0]  # bottom right to bottom left
        ):
            return cell[2, 2]
        return 0

    def game_over(self, board: np.ndarray = None) -> bool:
        if board is None:
            return self.game_winner(self.state.board) != 0
        return self.game_winner(board) != 0

    def game_winner(self, board: np.ndarray) -> int:
        big_cell = np.ndarray((3, 3))
        for i in range(3):
            for j in range(3):
                big_cell[i, j] = self.cell_winner(board[i, j])
        return self.cell_winner(big_cell)

    def reset(self) -> None:
        self.state = State()

    def print(self) -> None:
        self.state.print()


if __name__ == '__main__':
    game = Game()
    while True:
        game.print()
        position_str = input()
        if len(position_str) != 4:
            continue
        try:
            int(position_str)
        except ValueError:
            continue
        game.play((int(position_str[0]), int(position_str[1]), int(position_str[2]), int(position_str[3])))
        if game.game_over():
            game.print()
            break
