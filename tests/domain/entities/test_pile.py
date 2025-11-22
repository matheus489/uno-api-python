import pytest
from domain.entities.pile import Pile
from domain.entities.card import Card, CardColor, CardValue


class TestPile:
    """Testes para entidade Pile"""
    
    def test_pile_creation_empty(self):
        pile = Pile()
        assert len(pile.cards) == 0
        assert pile.is_empty() is True
        assert pile.size() == 0
    
    def test_pile_add_card(self):
        pile = Pile()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        pile.add_card(card)
        assert len(pile.cards) == 1
        assert pile.cards[0] == card
        assert pile.is_empty() is False
        assert pile.size() == 1
    
    def test_pile_get_top_card(self):
        pile = Pile()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        pile.add_card(card1)
        pile.add_card(card2)
        
        top = pile.get_top_card()
        assert top == card2
        assert len(pile.cards) == 2
    
    def test_pile_get_top_card_empty_returns_none(self):
        pile = Pile()
        top = pile.get_top_card()
        assert top is None
    
    def test_pile_pop_top_card(self):
        pile = Pile()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        pile.add_card(card1)
        pile.add_card(card2)
        
        popped = pile.pop_top_card()
        assert popped == card2
        assert len(pile.cards) == 1
        assert pile.cards[0] == card1
    
    def test_pile_pop_top_card_empty_returns_none(self):
        pile = Pile()
        popped = pile.pop_top_card()
        assert popped is None
    
    def test_pile_remove_all(self):
        pile = Pile()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        pile.add_card(card1)
        pile.add_card(card2)
        
        removed = pile.remove_all()
        assert len(removed) == 2
        assert removed == [card1, card2]
        assert pile.is_empty() is True
        assert pile.size() == 0
    
    def test_pile_size(self):
        pile = Pile()
        assert pile.size() == 0
        pile.add_card(Card(color=CardColor.RED, value=CardValue.ONE, id=1))
        assert pile.size() == 1
        pile.add_card(Card(color=CardColor.BLUE, value=CardValue.TWO, id=2))
        assert pile.size() == 2

