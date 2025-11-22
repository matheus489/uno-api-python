import pytest
from application.use_cases.pass_turn import PassTurnUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.deck import Deck
from domain.entities.card import Card, CardColor, CardValue


class TestPassTurnUseCase:
    """Testes para PassTurnUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.use_case = PassTurnUseCase(self.repository)
    
    def test_pass_turn_valid_game_and_player(self):
        game = Game(id=1)
        player = Player(id=0)
        game.add_player(player)
        game.add_player(Player(id=1))
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        
        initial_hand_size = len(player.hand.cards)
        initial_current_player = game.current_player
        
        self.repository.create(game)
        
        result = self.use_case.execute(1, 0)
        
        updated_game = self.repository.find_by_id(1)
        assert len(updated_game.get_player(0).hand.cards) == initial_hand_size + 1
        assert updated_game.current_player != initial_current_player
        assert result["message"] == "Vez passada. Uma carta foi adicionada à sua mão."
    
    def test_pass_turn_advances_to_next_player(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.add_player(Player(id=2))
        game.current_player = 0
        
        deck = Deck()
        deck.create_full_deck()
        game.deck = deck
        
        self.repository.create(game)
        
        self.use_case.execute(1, 0)
        
        updated_game = self.repository.find_by_id(1)
        assert updated_game.current_player == 1
    
    def test_pass_turn_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            self.use_case.execute(999, 0)
    
    def test_pass_turn_finished_game_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.is_finished = True
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="O jogo já foi finalizado"):
            self.use_case.execute(1, 0)
    
    def test_pass_turn_wrong_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.current_player = 0
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Não é a vez do jogador 1"):
            self.use_case.execute(1, 1)
    
    def test_pass_turn_non_existing_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.current_player = 5
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Jogador com ID 5 não encontrado"):
            self.use_case.execute(1, 5)

