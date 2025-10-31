from domain.entities.game import Game
from domain.repositories.game_repository import GameRepository
import random


class PassTurnUseCase:
    """Caso de uso: Passar a vez"""
    
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
    
    def execute(self, game_id: int, player_id: int) -> dict:
        """Passa a vez do jogador, adicionando uma carta à sua mão"""
        game = self.game_repository.find_by_id(game_id)
        
        if not game:
            raise ValueError(f"Jogo com ID {game_id} não encontrado")
        
        if game.is_finished:
            raise ValueError("O jogo já foi finalizado")
        
        # Verificar se é a vez do jogador
        if game.current_player != player_id:
            raise ValueError(f"Não é a vez do jogador {player_id}. Jogador da vez: {game.current_player}")
        
        player = game.get_player(player_id)
        
        if not player:
            raise ValueError(f"Jogador com ID {player_id} não encontrado")
        
        # Adicionar uma carta do baralho à mão do jogador
        if game.deck:
            card = game.deck.pop()
            player.add_card(card)
        
        # Passar para o próximo jogador
        game.next_player()
        self.game_repository.update(game)
        
        return {"message": "Vez passada. Uma carta foi adicionada à sua mão."}

