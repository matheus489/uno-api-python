from abc import ABC, abstractmethod
from domain.entities.game import Game

class GameObserver(ABC):
    @abstractmethod
    def update(self, game: Game):
        """Recebe a notificação de que o estado do jogo mudou"""
        pass