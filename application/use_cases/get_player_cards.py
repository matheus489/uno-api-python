from typing import List
from domain.entities.card import Card
from domain.repositories.game_repository import GameRepository


class GetPlayerCardsUseCase:
    """Caso de uso: Obter cartas de um jogador"""
    
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
    
    def execute(self, game_id: int, player_id: int) -> List[Card]:
        """Retorna as cartas de um jogador específico"""
        game = self.game_repository.find_by_id(game_id)
        
        if not game:
            raise ValueError(f"Jogo com ID {game_id} não encontrado")
        
        player = game.get_player(player_id)
        
        if not player:
            raise ValueError(f"Jogador com ID {player_id} não encontrado no jogo")
        
        return player.hand
