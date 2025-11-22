import pytest
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from domain.entities.game import Game
from domain.entities.player import Player


class TestInMemoryGameRepository:
    """Testes para InMemoryGameRepository"""
    
    def test_repository_creation(self):
        repo = InMemoryGameRepository()
        assert repo._games == {}
    
    def test_repository_create_game(self):
        repo = InMemoryGameRepository()
        game = Game(id=1)
        game.add_player(Player(id=0))
        
        created = repo.create(game)
        assert created == game
        assert repo.find_by_id(1) == game
        assert len(repo._games) == 1
    
    def test_repository_find_by_id_existing(self):
        repo = InMemoryGameRepository()
        game1 = Game(id=1)
        game2 = Game(id=2)
        repo.create(game1)
        repo.create(game2)
        
        found = repo.find_by_id(1)
        assert found == game1
        
        found = repo.find_by_id(2)
        assert found == game2
    
    def test_repository_find_by_id_non_existing(self):
        repo = InMemoryGameRepository()
        found = repo.find_by_id(999)
        assert found is None
    
    def test_repository_update_existing_game(self):
        repo = InMemoryGameRepository()
        game = Game(id=1)
        game.add_player(Player(id=0))
        repo.create(game)
        
        game.is_finished = True
        updated = repo.update(game)
        assert updated == game
        assert repo.find_by_id(1).is_finished is True
    
    def test_repository_update_non_existing_game_raises_error(self):
        repo = InMemoryGameRepository()
        game = Game(id=999)
        
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            repo.update(game)
    
    def test_repository_get_all_games(self):
        repo = InMemoryGameRepository()
        game1 = Game(id=1)
        game2 = Game(id=2)
        repo.create(game1)
        repo.create(game2)
        
        all_games = repo.get_all_games()
        assert len(all_games) == 2
        assert all_games[1] == game1
        assert all_games[2] == game2

