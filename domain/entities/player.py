from dataclasses import dataclass, field
from domain.entities.hand import Hand

@dataclass
class Player:
    """Entidade Jogador"""
    id: int
    hand: Hand = field(default_factory=Hand)