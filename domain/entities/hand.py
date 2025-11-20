from dataclasses import dataclass, field
from typing import List
from domain.entities.card import Card

@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)

    def add_card(self, card: Card):
        self.cards.append(card)
    
    def remove_card(self, card_index: int) -> Card:
        if 0 <= card_index < len(self.cards):
            return self.cards.pop(card_index)
        raise IndexError("Card index out of range")
    
    def is_empty(self) -> bool:
        return len(self.cards) == 0
    
    def get_card(self, card_index: int) -> Card:
        if 0 <= card_index < len(self.cards):
            return self.cards[card_index]
        raise IndexError("Card index out of range")
    
    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)