import pytest
from application.factories.effect_strategy_factory import EffectStrategyFactory
from application.strategies.card_effect_strategy import (
    NormalStrategy, SkipStrategy, ReverseStrategy, DrawTwoStrategy
)
from domain.entities.card import CardValue


class TestEffectStrategyFactory:
    """Testes para EffectStrategyFactory"""
    
    def test_get_strategy_skip(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.SKIP)
        assert isinstance(strategy, SkipStrategy)
    
    def test_get_strategy_reverse(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.REVERSE)
        assert isinstance(strategy, ReverseStrategy)
    
    def test_get_strategy_draw_two(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.DRAW_TWO)
        assert isinstance(strategy, DrawTwoStrategy)
    
    def test_get_strategy_normal_for_number_card(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.ONE)
        assert isinstance(strategy, NormalStrategy)
    
    def test_get_strategy_normal_for_zero(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.ZERO)
        assert isinstance(strategy, NormalStrategy)
    
    def test_get_strategy_normal_for_nine(self):
        strategy = EffectStrategyFactory.get_strategy(CardValue.NINE)
        assert isinstance(strategy, NormalStrategy)

