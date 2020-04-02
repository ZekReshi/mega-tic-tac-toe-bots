import MTTTBot
from Game import Game


class BvbTrainer:

    @staticmethod
    def train(player1: MTTTBot, player2: MTTTBot, games: int) -> None:
        game = Game()
        for _ in range(games):
            while not game.game_over():
                if game.state.turn:
                    player1.play(game)
                else:
                    player2.play(game)
            player1.game_over(game, not game.state.turn)
            player2.game_over(game, game.state.turn)
