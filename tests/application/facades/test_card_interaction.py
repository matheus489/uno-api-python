import pytest
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.entities.deck import Deck
from domain.entities.pile import Pile
from domain.entities.hand import Hand
from domain.entities.card import Card, CardColor, CardValue


class TestCardInteractionFacade:
    """Testes para CardInteractionFacade"""
    
    def test_facade_creation(self):
        facade = CardInteractionFacade()
        assert facade is not None
    
    def test_setup_new_game(self):
        facade = CardInteractionFacade()
        deck = Deck()
        pile = Pile()
        
        facade.setup_new_game(deck, pile)
        
        assert deck.is_empty() is False
        assert pile.is_empty() is False
        assert pile.size() == 1
    
    def test_deal_initial_hands(self):
        facade = CardInteractionFacade()
        deck = Deck()
        deck.create_full_deck()
        
        hands = facade.deal_initial_hands(num_players=3, deck=deck, cards_per_player=7)
        
        assert len(hands) == 3
        assert len(hands[0]) == 7
        assert len(hands[1]) == 7
        assert len(hands[2]) == 7
    
    def test_draw_card_from_non_empty_deck(self):
        facade = CardInteractionFacade()
        deck = Deck()
        pile = Pile()
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        deck.add_cards([card1, card2])
        
        drawn = facade.draw_card(deck, pile)
        assert drawn == card2
        assert len(deck.cards) == 1
    
    def test_draw_card_recycles_when_deck_empty(self):
        facade = CardInteractionFacade()
        deck = Deck()
        pile = Pile()
        top_card = Card(color=CardColor.GREEN, value=CardValue.THREE, id=3)
        other_card1 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        other_card2 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        
        pile.add_card(other_card2)
        pile.add_card(other_card1)
        pile.add_card(top_card)
        
        drawn = facade.draw_card(deck, pile)
        
        assert drawn is not None
        assert pile.get_top_card() == top_card
        assert pile.size() == 1
    
    def test_validate_move_same_color(self):
        facade = CardInteractionFacade()
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.RED, value=CardValue.TWO)
        
        assert facade.validate_move(play_card, top_card) is True
    
    def test_validate_move_same_value(self):
        facade = CardInteractionFacade()
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.BLUE, value=CardValue.ONE)
        
        assert facade.validate_move(play_card, top_card) is True
    
    def test_validate_move_different_color_and_value(self):
        facade = CardInteractionFacade()
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.BLUE, value=CardValue.TWO)
        
        assert facade.validate_move(play_card, top_card) is False
    
    def test_play_card(self):
        facade = CardInteractionFacade()
        pile = Pile()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        
        facade.play_card(card, pile)
        
        assert pile.size() == 1
        assert pile.get_top_card() == card
    
    def test_add_card_to_hand(self):
        facade = CardInteractionFacade()
        hand = Hand()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        
        facade.add_card_to_hand(hand, card)
        
        assert len(hand.cards) == 1
        assert hand.cards[0] == card
    
    def test_get_top_card(self):
        facade = CardInteractionFacade()
        pile = Pile()
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        pile.add_card(card)
        
        top = facade.get_top_card(pile)
        assert top == card

