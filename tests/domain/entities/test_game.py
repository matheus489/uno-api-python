import pytest
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.card import Card, CardColor, CardValue


class TestGame:
    """Testes para entidade Game"""
    
    def test_game_creation(self):
        game = Game(id=1)
        assert game.id == 1
        assert len(game.players) == 0
        assert game.current_player == 0
        assert game.is_finished is False
        assert game.winner_id is None
        assert game.direction == 1
    
    def test_game_add_player(self):
        game = Game(id=1)
        player = Player(id=0)
        game.add_player(player)
        assert len(game.players) == 1
        assert game.players[0] == player
    
    def test_game_get_player_valid_id(self):
        game = Game(id=1)
        player1 = Player(id=0)
        player2 = Player(id=1)
        game.add_player(player1)
        game.add_player(player2)
        
        retrieved = game.get_player(0)
        assert retrieved == player1
        
        retrieved = game.get_player(1)
        assert retrieved == player2
    
    def test_game_get_player_invalid_id_returns_none(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        
        assert game.get_player(10) is None
        assert game.get_player(-1) is None
    
    def test_game_next_player_forward(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        
        assert game.current_player == 0
        game.next_player()
        assert game.current_player == 1
        game.next_player()
        assert game.current_player == 2
        game.next_player()
        assert game.current_player == 0
    
    def test_game_next_player_backward(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.direction = -1
        
        assert game.current_player == 0
        game.next_player()
        assert game.current_player == 1
        game.next_player()
        assert game.current_player == 0
    
    def test_game_next_player_when_finished_does_not_change(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.is_finished = True
        game.current_player = 1
        
        game.next_player()
        assert game.current_player == 1
    
    def test_game_reverse_direction(self):
        game = Game(id=1)
        assert game.direction == 1
        game.reverse_direction()
        assert game.direction == -1
        game.reverse_direction()
        assert game.direction == 1

