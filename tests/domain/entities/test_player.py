import pytest
from domain.entities.player import Player
from domain.entities.hand import Hand
from domain.entities.card import Card, CardColor, CardValue


class TestPlayer:
    """Testes para entidade Player"""
    
    def test_player_creation(self):
        player = Player(id=0)
        assert player.id == 0
        assert isinstance(player.hand, Hand)
        assert player.hand.is_empty() is True
    
    def test_player_add_hand(self):
        player = Player(id=0)
        new_hand = Hand()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        new_hand.add_card(card)
        
        player.add_hand(new_hand)
        assert player.hand == new_hand
        assert len(player.hand.cards) == 1
    
    def test_player_with_multiple_cards(self):
        player = Player(id=1)
        cards = [
            Card(color=CardColor.RED, value=CardValue.ONE, id=1),
            Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        ]
        player.hand.add_cards(cards)
        assert len(player.hand.cards) == 2

