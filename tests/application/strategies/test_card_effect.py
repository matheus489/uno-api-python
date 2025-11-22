import pytest
from application.strategies.card_effect_strategy import (
    NormalStrategy, SkipStrategy, ReverseStrategy, DrawTwoStrategy
)
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.deck import Deck
from application.facades.CardInteractionFacade import CardInteractionFacade


class TestNormalStrategy:
    """Testes para NormalStrategy"""
    
    def test_normal_strategy_advances_one_player(self):
        strategy = NormalStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        facade = CardInteractionFacade()
        
        original_current = game.current_player
        strategy.apply(game, facade)
        
        assert game.current_player == (original_current + 1) % 3


class TestSkipStrategy:
    """Testes para SkipStrategy"""
    
    def test_skip_strategy_advances_two_players(self):
        strategy = SkipStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        facade = CardInteractionFacade()
        
        original_current = game.current_player
        strategy.apply(game, facade)
        
        assert game.current_player == (original_current + 2) % 3
    
    def test_skip_strategy_with_two_players(self):
        strategy = SkipStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        facade = CardInteractionFacade()
        
        original_current = game.current_player
        strategy.apply(game, facade)
        
        assert game.current_player == original_current


class TestReverseStrategy:
    """Testes para ReverseStrategy"""
    
    def test_reverse_strategy_with_two_players_acts_as_skip(self):
        strategy = ReverseStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        facade = CardInteractionFacade()
        
        original_current = game.current_player
        strategy.apply(game, facade)
        
        assert game.current_player == original_current
        assert game.direction == 1
    
    def test_reverse_strategy_with_more_than_two_players(self):
        strategy = ReverseStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        facade = CardInteractionFacade()
        
        original_direction = game.direction
        original_current = game.current_player
        
        strategy.apply(game, facade)
        
        assert game.direction == -original_direction
        assert game.current_player == (original_current - 1) % 3
    
    def test_reverse_strategy_reverses_direction_multiple_times(self):
        strategy = ReverseStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        facade = CardInteractionFacade()
        
        strategy.apply(game, facade)
        assert game.direction == -1
        
        strategy.apply(game, facade)
        assert game.direction == 1


class TestDrawTwoStrategy:
    """Testes para DrawTwoStrategy"""
    
    def test_draw_two_strategy_adds_two_cards_and_skips_turn(self):
        strategy = DrawTwoStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        
        victim = game.get_player(1)
        initial_hand_size = len(victim.hand.cards)
        
        facade = CardInteractionFacade()
        original_current = game.current_player
        
        strategy.apply(game, facade)
        
        assert len(victim.hand.cards) == initial_hand_size + 2
        assert game.current_player == (original_current + 2) % 2
    
    def test_draw_two_strategy_with_three_players(self):
        strategy = DrawTwoStrategy()
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        
        victim = game.get_player(1)
        initial_hand_size = len(victim.hand.cards)
        
        facade = CardInteractionFacade()
        original_current = game.current_player
        
        strategy.apply(game, facade)
        
        assert len(victim.hand.cards) == initial_hand_size + 2
        assert game.current_player == (original_current + 2) % 3

