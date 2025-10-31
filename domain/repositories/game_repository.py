from abc import ABC, abstractmethod
from typing import Optional
from ..entities.game import Game


class GameRepository(ABC):
    """Interface do repositório de jogos"""
    
    @abstractmethod
    def create(self, game: Game) -> Game:
        """Cria um novo jogo"""
        pass
    
    @abstractmethod
    def find_by_id(self, game_id: int) -> Optional[Game]:
        """Busca um jogo pelo ID"""
        pass
    
    @abstractmethod
    def update(self, game: Game) -> Game:
        """Atualiza um jogo"""
        pass

