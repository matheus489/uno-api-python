from dataclasses import dataclass, field
from typing import List
from domain.entities.card import Card

@dataclass
class Pile:
    cards: List[Card] = field(default_factory=list)

    def add_card(self, card: Card):
        self.cards.append(card)
    
    def size(self) -> int:
        return len(self.cards)
    
    def is_empty(self) -> bool:
        return len(self.cards) == 0
    
    def pop_top_card(self) -> Card:
        if not self.is_empty():
            return self.cards.pop()
        
    def get_top_card(self) -> Card:
        if not self.is_empty():
            return self.cards[-1]
        return None
        
    def remove_all(self) -> List[Card]:
        removed_cards = self.cards[:]
        self.cards = []
        return removed_cards