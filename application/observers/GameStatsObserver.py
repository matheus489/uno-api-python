from .GameObserver import GameObserver
from domain.entities.game import Game

class GameStatsObserver(GameObserver):
    _instance = None

    def __new__(cls):
        # Padrão Singleton para garantir que só existe UM contador na memória
        if cls._instance is None:
            cls._instance = super(GameStatsObserver, cls).__new__(cls)
            cls._instance.games_finished_count = 0
            cls._instance.last_winner_id = None
        return cls._instance

    def update(self, game: Game):
        if game.is_finished:
            self.games_finished_count += 1
            self.last_winner_id = game.winner_id
            print(f"[Observer] Jogo finalizado! Total: {self.games_finished_count}")

    def get_stats(self):
        return {
            "total_games_finished": self.games_finished_count,
            "last_winner_id": self.last_winner_id
        }