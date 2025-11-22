import pytest
from domain.entities.hand import Hand
from domain.entities.card import Card, CardColor, CardValue


class TestHand:
    """Testes para entidade Hand"""
    
    def test_hand_creation_empty(self):
        hand = Hand()
        assert len(hand.cards) == 0
        assert hand.is_empty() is True
    
    def test_hand_add_card(self):
        hand = Hand()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        hand.add_card(card)
        assert len(hand.cards) == 1
        assert hand.cards[0] == card
        assert hand.is_empty() is False
    
    def test_hand_remove_card(self):
        hand = Hand()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        hand.add_card(card1)
        hand.add_card(card2)
        
        removed = hand.remove_card(0)
        assert removed == card1
        assert len(hand.cards) == 1
        assert hand.cards[0] == card2
    
    def test_hand_remove_card_invalid_index_raises_error(self):
        hand = Hand()
        hand.add_card(Card(color=CardColor.RED, value=CardValue.ONE, id=1))
        
        with pytest.raises(IndexError):
            hand.remove_card(10)
        
        with pytest.raises(IndexError):
            hand.remove_card(-1)
    
    def test_hand_get_card(self):
        hand = Hand()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        hand.add_card(card)
        
        retrieved = hand.get_card(0)
        assert retrieved == card
    
    def test_hand_get_card_invalid_index_raises_error(self):
        hand = Hand()
        hand.add_card(Card(color=CardColor.RED, value=CardValue.ONE, id=1))
        
        with pytest.raises(IndexError):
            hand.get_card(10)
        
        with pytest.raises(IndexError):
            hand.get_card(-1)
    
    def test_hand_add_cards(self):
        hand = Hand()
        cards = [
            Card(color=CardColor.RED, value=CardValue.ONE, id=1),
            Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        ]
        hand.add_cards(cards)
        assert len(hand.cards) == 2
        assert hand.cards == cards
    
    def test_hand_is_empty(self):
        hand = Hand()
        assert hand.is_empty() is True
        hand.add_card(Card(color=CardColor.RED, value=CardValue.ONE, id=1))
        assert hand.is_empty() is False

