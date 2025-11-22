import pytest
from application.use_cases.play_card import PlayCardUseCase
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade
from application.factories.effect_strategy_factory import EffectStrategyFactory
from application.observers.GameStatsObserver import GameStatsObserver
from domain.entities.game import Game
from domain.entities.player import Player
from domain.entities.card import Card, CardColor, CardValue


class TestPlayCardUseCase:
    """Testes para PlayCardUseCase"""
    
    def setup_method(self):
        self.repository = InMemoryGameRepository()
        self.card_facade = CardInteractionFacade()
        self.strategy_factory = EffectStrategyFactory()
        self.use_case = PlayCardUseCase(
            self.repository,
            self.card_facade,
            self.strategy_factory
        )
    
    def test_play_card_valid_move(self):
        game = Game(id=1)
        player = Player(id=0)
        top_card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        playable_card1 = Card(color=CardColor.RED, value=CardValue.TWO, id=2)
        playable_card2 = Card(color=CardColor.BLUE, value=CardValue.THREE, id=3)
        
        player.hand.add_card(playable_card1)
        player.hand.add_card(playable_card2)
        game.add_player(player)
        game.discard_pile.add_card(top_card)
        
        self.repository.create(game)
        
        result = self.use_case.execute(1, 0, 0)
        
        updated_game = self.repository.find_by_id(1)
        assert len(updated_game.get_player(0).hand.cards) == 1
        assert result["message"] == "Carta jogada com sucesso"
        assert result["won"] is False
    
    def test_play_card_player_wins(self):
        game = Game(id=1)
        player = Player(id=0)
        top_card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        last_card = Card(color=CardColor.RED, value=CardValue.TWO, id=2)
        
        player.hand.add_card(last_card)
        game.add_player(player)
        game.discard_pile.add_card(top_card)
        
        self.repository.create(game)
        
        result = self.use_case.execute(1, 0, 0)
        
        updated_game = self.repository.find_by_id(1)
        assert updated_game.is_finished is True
        assert updated_game.winner_id == 0
        assert result["message"] == "Você ganhou o jogo!"
        assert result["won"] is True
    
    def test_play_card_non_existing_game_raises_error(self):
        with pytest.raises(ValueError, match="Jogo com ID 999 não encontrado"):
            self.use_case.execute(999, 0, 0)
    
    def test_play_card_finished_game_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.is_finished = True
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="O jogo já foi finalizado"):
            self.use_case.execute(1, 0, 0)
    
    def test_play_card_wrong_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.add_player(Player(id=1))
        game.current_player = 0
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Não é a vez do jogador 1"):
            self.use_case.execute(1, 1, 0)
    
    def test_play_card_non_existing_player_raises_error(self):
        game = Game(id=1)
        game.add_player(Player(id=0))
        game.current_player = 5
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Jogador com ID 5 não encontrado"):
            self.use_case.execute(1, 5, 0)
    
    def test_play_card_invalid_card_index_raises_error(self):
        game = Game(id=1)
        player = Player(id=0)
        player.hand.add_card(Card(color=CardColor.RED, value=CardValue.ONE, id=1))
        game.add_player(player)
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="Índice de carta inválido"):
            self.use_case.execute(1, 0, 10)
    
    def test_play_card_invalid_move_raises_error(self):
        game = Game(id=1)
        player = Player(id=0)
        top_card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        invalid_card = Card(color=CardColor.BLUE, value=CardValue.TWO, id=2)
        
        player.hand.add_card(invalid_card)
        game.add_player(player)
        game.discard_pile.add_card(top_card)
        
        self.repository.create(game)
        
        with pytest.raises(ValueError, match="A carta não pode ser jogada"):
            self.use_case.execute(1, 0, 0)
    
    def test_play_card_notifies_observers_when_game_finished(self):
        GameStatsObserver._instance = None
        observer = GameStatsObserver()
        
        game = Game(id=1)
        player = Player(id=0)
        top_card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        last_card = Card(color=CardColor.RED, value=CardValue.TWO, id=2)
        
        player.hand.add_card(last_card)
        game.add_player(player)
        game.discard_pile.add_card(top_card)
        
        self.repository.create(game)
        self.use_case.attach_observer(observer)
        
        result = self.use_case.execute(1, 0, 0)
        
        stats = observer.get_stats()
        assert result["won"] is True
        assert stats["total_games_finished"] == 1
        assert stats["last_winner_id"] == 0

