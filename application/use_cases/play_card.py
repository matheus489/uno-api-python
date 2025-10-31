from domain.entities.game import Game
from domain.entities.card import Card
from domain.repositories.game_repository import GameRepository


class PlayCardUseCase:
    """Caso de uso: Jogar uma carta"""
    
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
    
    def execute(self, game_id: int, player_id: int, card_index: int) -> dict:
        """Joga uma carta de um jogador"""
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
        
        # Verificar se o índice é válido
        if card_index < 0 or card_index >= len(player.hand):
            raise ValueError(f"Índice de carta inválido: {card_index}")
        
        card_to_play = player.hand[card_index]
        top_card = game.get_top_card()
        
        # Verificar se a carta pode ser jogada
        if not card_to_play.can_play_on(top_card):
            raise ValueError(f"A carta não pode ser jogada. Carta do topo: {top_card}, Carta escolhida: {card_to_play}")
        
        # Remover carta da mão do jogador
        player.remove_card(card_index)
        
        # Adicionar carta à pilha
        game.play_card(card_to_play)
        
        # Verificar se o jogador ganhou
        if not player.has_cards():
            game.is_finished = True
            game.winner_id = player_id
            self.game_repository.update(game)
            return {"message": "Você ganhou o jogo!", "won": True}
        
        # Passar para o próximo jogador
        game.next_player()
        self.game_repository.update(game)
        
        return {"message": "Carta jogada com sucesso", "won": False}

