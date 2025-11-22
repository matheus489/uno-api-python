import pytest
from domain.entities.card import Card, CardColor, CardValue


class TestCardColor:
    """Testes para CardColor enum"""
    
    def test_card_color_values(self):
        assert CardColor.RED == "vermelho"
        assert CardColor.BLUE == "azul"
        assert CardColor.GREEN == "verde"
        assert CardColor.YELLOW == "amarelo"
    
    def test_card_color_enum_members(self):
        assert len(list(CardColor)) == 4


class TestCardValue:
    """Testes para CardValue enum"""
    
    def test_card_value_numbers(self):
        assert CardValue.ZERO == "0"
        assert CardValue.ONE == "1"
        assert CardValue.NINE == "9"
    
    def test_card_value_special_cards(self):
        assert CardValue.SKIP == "pular"
        assert CardValue.REVERSE == "reverter"
        assert CardValue.DRAW_TWO == "+2"


class TestCard:
    """Testes para entidade Card"""
    
    def test_card_creation(self):
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        assert card.color == CardColor.RED
        assert card.value == CardValue.ONE
        assert card.id == 1
    
    def test_card_repr(self):
        card = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        assert str(card) == "azul 2"
    
    def test_card_can_play_on_same_color(self):
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.RED, value=CardValue.TWO)
        assert play_card.can_play_on(top_card) is True
    
    def test_card_can_play_on_same_value(self):
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.BLUE, value=CardValue.ONE)
        assert play_card.can_play_on(top_card) is True
    
    def test_card_cannot_play_on_different_color_and_value(self):
        top_card = Card(color=CardColor.RED, value=CardValue.ONE)
        play_card = Card(color=CardColor.BLUE, value=CardValue.TWO)
        assert play_card.can_play_on(top_card) is False
    
    def test_card_default_id_is_none(self):
        card = Card(color=CardColor.GREEN, value=CardValue.THREE)
        assert card.id is None

