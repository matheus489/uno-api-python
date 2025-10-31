from typing import Dict, Optional
from domain.entities.game import Game
from domain.repositories.game_repository import GameRepository


class InMemoryGameRepository(GameRepository):
    """Implementação em memória do repositório de jogos"""
    
    def __init__(self):
        self._games: Dict[int, Game] = {}
    
    def create(self, game: Game) -> Game:
        """Cria um novo jogo"""
        self._games[game.id] = game
        return game
    
    def find_by_id(self, game_id: int) -> Optional[Game]:
        """Busca um jogo pelo ID"""
        return self._games.get(game_id)
    
    def update(self, game: Game) -> Game:
        """Atualiza um jogo"""
        if game.id not in self._games:
            raise ValueError(f"Jogo com ID {game.id} não encontrado")
        self._games[game.id] = game
        return game
    
    def get_all_games(self) -> Dict[int, Game]:
        """Retorna todos os jogos (método auxiliar para debugging)"""
        return self._games

