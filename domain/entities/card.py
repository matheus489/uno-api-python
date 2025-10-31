from enum import Enum
from dataclasses import dataclass


class CardColor(str, Enum):
    """Cores das cartas do UNO"""
    RED = "vermelho"
    BLUE = "azul"
    GREEN = "verde"
    YELLOW = "amarelo"
    WILD = "coringa"


class CardValue(str, Enum):
    """Valores das cartas do UNO"""
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    SKIP = "pular"
    REVERSE = "reverter"
    DRAW_TWO = "+2"
    WILD = "coringa"
    WILD_DRAW_FOUR = "+4"


@dataclass
class Card:
    """Entidade Carta do UNO"""
    color: CardColor
    value: CardValue
    id: int = None
    
    def __repr__(self):
        return f"{self.color.value} {self.value.value}"
    
    def can_play_on(self, other_card: 'Card') -> bool:
        """Verifica se esta carta pode ser jogada sobre outra carta"""
        if self.color == CardColor.WILD or other_card.color == CardColor.WILD:
            return True
        return self.color == other_card.color or self.value == other_card.value

