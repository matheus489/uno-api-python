from dataclasses import dataclass, field
from typing import List, Optional
from .card import Card
from .deck import Deck
from .pile import Pile
from .player import Player





@dataclass
class Game:
    """Entidade Jogo UNO"""
    id: int
    players: List[Player] = field(default_factory=list)
    current_player: int = 0
    deck: Deck = field(default_factory=Deck)
    discard_pile: Pile = field(default_factory=Pile)
    is_finished: bool = False
    winner_id: Optional[int] = None
    direction: int = 1

    def reverse_direction(self):
        self.direction *= -1
    
    def add_player(self, player: Player):
        """Adiciona um jogador ao jogo"""
        self.players.append(player)
    
    def get_player(self, player_id: int) -> Optional[Player]:
        """Retorna um jogador pelo ID"""
        if 0 <= player_id < len(self.players):
            return self.players[player_id]
        return None
    
    def next_player(self):
        """Passa para o próximo jogador"""
        if not self.is_finished:
            total_players = len(self.players)
            self.current_player = (self.current_player + self.direction) % total_players
    
    def play_card(self, card: Card):
        """Adiciona uma carta à pilha"""
        self.pile.append(card)

