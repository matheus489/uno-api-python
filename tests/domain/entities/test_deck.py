import pytest
from domain.entities.deck import Deck
from domain.entities.card import Card, CardColor, CardValue


class TestDeck:
    """Testes para entidade Deck"""
    
    def test_deck_creation_empty(self):
        deck = Deck()
        assert len(deck.cards) == 0
        assert deck.is_empty() is True
    
    def test_deck_add_cards(self):
        deck = Deck()
        cards = [
            Card(color=CardColor.RED, value=CardValue.ONE, id=1),
            Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        ]
        deck.add_cards(cards)
        assert len(deck.cards) == 2
        assert deck.is_empty() is False
    
    def test_deck_create_full_deck(self):
        deck = Deck()
        deck.create_full_deck()
        assert deck.is_empty() is False
        assert len(deck.cards) > 0
    
    def test_deck_create_full_deck_card_count(self):
        deck = Deck()
        deck.create_full_deck()
        total_cards = len(deck.cards)
        # 4 cores * (1 zero + 9 números * 2 + 3 ações * 2) = 4 * 25 = 100
        assert total_cards == 100
    
    def test_deck_draw_card(self):
        deck = Deck()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        deck.add_cards([card1, card2])
        
        drawn = deck.draw()
        assert drawn == card2
        assert len(deck.cards) == 1
        assert deck.cards[0] == card1
    
    def test_deck_draw_from_empty_returns_none(self):
        deck = Deck()
        drawn = deck.draw()
        assert drawn is None
    
    def test_deck_shuffle(self):
        deck = Deck()
        deck.create_full_deck()
        original_order = deck.cards[:]
        deck.shuffle()
        assert len(deck.cards) == len(original_order)
        # Verifica que tem as mesmas cartas (comparando por id)
        original_ids = [card.id for card in original_order]
        shuffled_ids = [card.id for card in deck.cards]
        assert sorted(original_ids) == sorted(shuffled_ids)
    
    def test_deck_is_empty(self):
        deck = Deck()
        assert deck.is_empty() is True
        deck.add_cards([Card(color=CardColor.RED, value=CardValue.ONE, id=1)])
        assert deck.is_empty() is False

