from typing import List
from domain.entities.card import Card, CardColor, CardValue
from dataclasses import dataclass, field

@dataclass
class Deck:
    cards: List[Card] = field(default_factory=list)

    def create_full_deck(self):
        """Cria um baralho completo do UNO"""
        self.cards = []
        card_id = 0
        
        # Cores normais (vermelho, azul, verde, amarelo)
        colors = [CardColor.RED, CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW]
        
        for color in colors:
            # Uma carta de valor 0
            self.cards.append(Card(id=card_id, color=color, value=CardValue.ZERO))
            card_id += 1
            
            # Duas cartas de cada número (1-9)
            for value in [CardValue.ONE, CardValue.TWO, CardValue.THREE, CardValue.FOUR,
                         CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE]:
                self.cards.append(Card(id=card_id, color=color, value=value))
                card_id += 1
                self.cards.append(Card(id=card_id, color=color, value=value))
                card_id += 1
            
            # # Duas cartas de cada ação
            # for value in [CardValue.SKIP, CardValue.REVERSE, CardValue.DRAW_TWO]:
            #     deck.append(Card(id=card_id, color=color, value=value))
            #     card_id += 1
            #     deck.append(Card(id=card_id, color=color, value=value))
            #     card_id += 1
        
        # # Cartas coringa
        # for _ in range(4):
        #     self.cards.append(Card(id=card_id, color=CardColor.WILD, value=CardValue.WILD))
        #     card_id += 1
        
        # for _ in range(4):
        #     self.cards.append(Card(id=card_id, color=CardColor.WILD, value=CardValue.WILD_DRAW_FOUR))
        #     card_id += 1

    def draw(self) -> Card:
        if not self.is_empty():
            return self.cards.pop()
        
    def shuffle(self):
        import random
        random.shuffle(self.cards)


    def is_empty(self) -> bool:
        return len(self.cards) == 0
    
    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)