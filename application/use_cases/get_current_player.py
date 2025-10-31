from domain.repositories.game_repository import GameRepository


class GetCurrentPlayerUseCase:
    """Caso de uso: Obter jogador da vez"""
    
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
    
    def execute(self, game_id: int) -> int:
        """Retorna o ID do jogador da vez"""
        game = self.game_repository.find_by_id(game_id)
        
        if not game:
            raise ValueError(f"Jogo com ID {game_id} não encontrado")
        
        return game.current_player

