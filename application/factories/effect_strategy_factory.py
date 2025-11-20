from application.strategies.card_effect_strategy import CardEffectStrategy, SkipStrategy, ReverseStrategy, DrawTwoStrategy, NormalStrategy
from domain.entities.card import CardValue

class EffectStrategyFactory:
    @staticmethod
    def get_strategy(card_value: CardValue) -> CardEffectStrategy:
        # Implementação de um factory simples para retornar a estratégia correta
        if card_value == CardValue.SKIP:
            return SkipStrategy()
        elif card_value == CardValue.REVERSE:
            return ReverseStrategy()
        elif card_value == CardValue.DRAW_TWO:
            return DrawTwoStrategy()
        
        return NormalStrategy()
        