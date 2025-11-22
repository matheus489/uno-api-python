import pytest
from application.use_cases.draw_card import DrawCardUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.deck import Deck
from domain.entities.pile import Pile


class TestDrawCardUseCase:
    """Testes para DrawCardUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.card_facade = CardInteractionFacade()
        self.use_case = DrawCardUseCase(self.repository, self.card_facade)
    
    def test_draw_card_valid_game_and_player(self):
        game = Game(id=1)
        player = Player(id=0)
        game.add_player(player)
        game.add_player(Player(id=1))
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        game.discard_pile = Pile()
        
        initial_hand_size = len(player.hand.cards)
        self.repository.create(game)
        
        drawn_card = self.use_case.execute(1, 0)
        
        updated_game = self.repository.find_by_id(1)
        assert drawn_card is not None
        assert len(updated_game.get_player(0).hand.cards) == initial_hand_size + 1
        assert drawn_card in updated_game.get_player(0).hand.cards
    
    def test_draw_card_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            self.use_case.execute(999, 0)
    
    def test_draw_card_wrong_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.current_player = 0
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        game.discard_pile = Pile()
        
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Não é a vez do jogador 1"):
            self.use_case.execute(1, 1)
    
    def test_draw_card_non_existing_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.current_player = 5
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        game.discard_pile = Pile()
        
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Jogador com ID 5 não encontrado"):
            self.use_case.execute(1, 5)
    
    def test_draw_card_empty_deck_recycles(self):
        game = Game(id=1)
        player = Player(id=0)
        game.add_player(player)
        
        deck = Deck()
        deck.create_full_deck()
        pile = Pile()
        top_card = deck.draw()
        pile.add_card(top_card)
        
        while not deck.is_empty():
            card = deck.draw()
            if card:
                pile.add_card(card)
        
        pile.pop_top_card()
        pile.add_card(top_card)
        
        game.deck = deck
        game.discard_pile = pile
        
        self.repository.create(game)
        
        drawn_card = self.use_case.execute(1, 0)
        assert drawn_card is not None

