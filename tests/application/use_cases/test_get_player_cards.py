import pytest
from application.use_cases.get_player_cards import GetPlayerCardsUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.card import Card, CardColor, CardValue


class TestGetPlayerCardsUseCase:
    """Testes para GetPlayerCardsUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.use_case = GetPlayerCardsUseCase(self.repository)
    
    def test_get_player_cards_existing_game_and_player(self):
        game = Game(id=1)
        player = Player(id=0)
        card1 = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        card2 = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        player.hand.add_card(card1)
        player.hand.add_card(card2)
        game.add_player(player)
        self.repository.create(game)
        
        cards = self.use_case.execute(1, 0)
        
        assert len(cards) == 2
        assert card1 in cards
        assert card2 in cards
    
    def test_get_player_cards_empty_hand(self):
        game = Game(id=1)
        player = Player(id=0)
        game.add_player(player)
        self.repository.create(game)
        
        cards = self.use_case.execute(1, 0)
        
        assert len(cards) == 0
    
    def test_get_player_cards_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            self.use_case.execute(999, 0)
    
    def test_get_player_cards_non_existing_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Jogador com ID 5 não encontrado"):
            self.use_case.execute(1, 5)

