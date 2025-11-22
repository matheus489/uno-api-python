import pytest
from application.observers.GameStatsObserver import GameStatsObserver
from domain.entities.game import Game
from domain.entities.player import Player


class TestGameStatsObserver:
    """Testes para GameStatsObserver"""
    
    def setup_method(self):
        GameStatsObserver._instance = None
    
    def test_singleton_pattern(self):
        observer1 = GameStatsObserver()
        observer2 = GameStatsObserver()
        
        assert observer1 is observer2
        assert id(observer1) == id(observer2)
    
    def test_initial_stats(self):
        observer = GameStatsObserver()
        
        stats = observer.get_stats()
        assert stats["total_games_finished"] == 0
        assert stats["last_winner_id"] is None
    
    def test_update_with_finished_game(self):
        observer = GameStatsObserver()
        
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.is_finished = True
        game.winner_id = 0
        
        observer.update(game)
        
        stats = observer.get_stats()
        assert stats["total_games_finished"] == 1
        assert stats["last_winner_id"] == 0
    
    def test_update_with_non_finished_game(self):
        observer = GameStatsObserver()
        
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.is_finished = False
        
        observer.update(game)
        
        stats = observer.get_stats()
        assert stats["total_games_finished"] == 0
    
    def test_multiple_finished_games(self):
        observer = GameStatsObserver()
        
        game1 = Game(id=1)
        game1.add_player(Player(id=0))
        game1.is_finished = True
        game1.winner_id = 0
        
        game2 = Game(id=2)
        game2.add_player(Player(id=0))
        game2.add_player(Player(id=1))
        game2.is_finished = True
        game2.winner_id = 1
        
        observer.update(game1)
        observer.update(game2)
        
        stats = observer.get_stats()
        assert stats["total_games_finished"] == 2
        assert stats["last_winner_id"] == 1

