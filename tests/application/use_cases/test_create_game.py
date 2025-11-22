import pytest
from application.use_cases.create_game import CreateGameUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.entities.card import Card, CardColor, CardValue


class TestCreateGameUseCase:
    """Testes para CreateGameUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.card_facade = CardInteractionFacade()
        self.use_case = CreateGameUseCase(self.repository, self.card_facade)
    
    def test_create_game_with_valid_number_of_players(self):
        game = self.use_case.execute(2)
        
        assert game is not None
        assert game.id == 1
        assert len(game.players) == 2
        assert game.current_player == 0
        assert game.is_finished is False
    
    def test_create_game_with_three_players(self):
        game = self.use_case.execute(3)
        
        assert len(game.players) == 3
        assert game.players[0].id == 0
        assert game.players[1].id == 1
        assert game.players[2].id == 2
    
    def test_create_game_distributes_cards(self):
        game = self.use_case.execute(2)
        
        for player in game.players:
            assert len(player.hand.cards) == 7
    
    def test_create_game_sets_up_deck_and_pile(self):
        game = self.use_case.execute(2)
        
        assert game.deck.is_empty() is False
        assert game.discard_pile.is_empty() is False
        assert game.discard_pile.size() == 1
    
    def test_create_game_saves_to_repository(self):
        game = self.use_case.execute(2)
        
        saved_game = self.repository.find_by_id(game.id)
        assert saved_game is not None
        assert saved_game.id == game.id
    
    def test_create_game_with_invalid_number_of_players_raises_error(self):
        with pytest.raises(ValueError, match="É necessário pelo menos 2 jogadores"):
            self.use_case.execute(1)
        
        with pytest.raises(ValueError, match="É necessário pelo menos 2 jogadores"):
            self.use_case.execute(0)
        
        with pytest.raises(ValueError, match="É necessário pelo menos 2 jogadores"):
            self.use_case.execute(-1)
    
    def test_create_multiple_games_increments_id(self):
        game1 = self.use_case.execute(2)
        game2 = self.use_case.execute(2)
        game3 = self.use_case.execute(2)
        
        assert game1.id == 1
        assert game2.id == 2
        assert game3.id == 3

