import pytest
from application.use_cases.get_current_player import GetCurrentPlayerUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from domain.entities.game import Game
from domain.entities.player import Player


class TestGetCurrentPlayerUseCase:
    """Testes para GetCurrentPlayerUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.use_case = GetCurrentPlayerUseCase(self.repository)
    
    def test_get_current_player_existing_game(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.current_player = 1
        self.repository.create(game)
        
        current_player_id = self.use_case.execute(1)
        
        assert current_player_id == 1
    
    def test_get_current_player_default_is_zero(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        self.repository.create(game)
        
        current_player_id = self.use_case.execute(1)
        
        assert current_player_id == 0
    
    def test_get_current_player_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            self.use_case.execute(999)

