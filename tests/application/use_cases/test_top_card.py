import pytest
from application.use_cases.top_card import TopCardUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.entities.game import Game
from domain.entities.card import Card, CardColor, CardValue


class TestTopCardUseCase:
    """Testes para TopCardUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.card_facade = CardInteractionFacade()
        self.use_case = TopCardUseCase(self.repository, self.card_facade)
    
    def test_get_top_card_existing_game(self):
        game = Game(id=1)
        top_card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        game.discard_pile.add_card(top_card)
        self.repository.create(game)
        
        result = self.use_case.execute(1)
        
        assert result == top_card
    
    def test_get_top_card_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo não encontrado"):
            self.use_case.execute(999)
    
    def test_get_top_card_with_multiple_cards_returns_top(self):
        game = Game(id=1)
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        game.discard_pile.add_card(card1)
        game.discard_pile.add_card(card2)
        self.repository.create(game)
        
        result = self.use_case.execute(1)
        
        assert result == card2

