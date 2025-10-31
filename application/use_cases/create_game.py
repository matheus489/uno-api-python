from typing import List
from domain.entities.game import Game, Player
from domain.entities.card import Card
from domain.repositories.game_repository import GameRepository
from application.services.deck_service import DeckService


class CreateGameUseCase:
    """Caso de uso: Criar um novo jogo"""
    
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
        self.deck_service = DeckService()
        self.next_game_id = 1
    
    def execute(self, num_players: int) -> Game:
        """Cria um novo jogo com o número especificado de jogadores"""
        # Validar número de jogadores
        if num_players < 2:
            raise ValueError("É necessário pelo menos 2 jogadores para iniciar um jogo")
        
        # Criar o jogo
        game = Game(id=self.next_game_id)
        self.next_game_id += 1
        
        # Criar e embaralhar o baralho
        deck = self.deck_service.create_deck()
        self.deck_service.shuffle(deck)
        
        # Distribuir cartas
        hands = self.deck_service.deal_cards(deck, num_players, cards_per_player=5)
        
        # Criar jogadores com suas cartas
        for i in range(num_players):
            player = Player(id=i)
            player.hand = hands[i]
            game.add_player(player)
        
        # Configurar baralho e pilha do jogo
        game.deck = deck
        if deck:
            game.pile.append(deck.pop())
        
        # Salvar o jogo
        self.game_repository.create(game)
        
        return game

