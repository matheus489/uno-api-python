from typing import List
from application.observers.GameObserver import GameObserver
from domain.entities.game import Game
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.repositories.game_repository import GameRepository


class PlayCardUseCase:
    """Caso de uso: Jogar uma carta"""
    
    def __init__(self, game_repository: GameRepository, card_facade: CardInteractionFacade):
        self.game_repository = game_repository
        self.card_facade = card_facade
        self.observers: List[GameObserver] = []

    def attach_observer(self, observer: GameObserver):
        """Anexa um observador ao caso de uso"""
        self.observers.append(observer)

    def notify_observers(self, game: Game):
        """Notifica todos os observadores sobre uma mudança no jogo"""
        for observer in self.observers:
            observer.update(game)
    
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
        if card_index < 0 or card_index >= len(player.hand.cards):
            raise ValueError(f"Índice de carta inválido: {card_index}")
        
        card_to_play = player.hand.get_card(card_index)
        top_card = self.card_facade.get_top_card(game.discard_pile)
        
        # Verificar se a carta pode ser jogada
        if not self.card_facade.validate_move(card_to_play, top_card):
            raise ValueError(f"A carta não pode ser jogada. Carta do topo: {top_card}, Carta escolhida: {card_to_play}")
        
        # Remover carta da mão do jogador
        player.hand.remove_card(card_index)
        
        # Adicionar carta à pilha
        self.card_facade.play_card(card_to_play, game.discard_pile)
        
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

