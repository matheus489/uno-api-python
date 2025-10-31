from dataclasses import dataclass, field
from typing import List, Optional
from .card import Card


@dataclass
class Player:
    """Entidade Jogador"""
    id: int
    hand: List[Card] = field(default_factory=list)
    
    def add_card(self, card: Card):
        """Adiciona uma carta à mão do jogador"""
        self.hand.append(card)
    
    def remove_card(self, card_index: int) -> Optional[Card]:
        """Remove uma carta da mão do jogador"""
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None
    
    def has_cards(self) -> bool:
        """Verifica se o jogador ainda tem cartas"""
        return len(self.hand) > 0


@dataclass
class Game:
    """Entidade Jogo UNO"""
    id: int
    players: List[Player] = field(default_factory=list)
    current_player: int = 0
    deck: List[Card] = field(default_factory=list)
    pile: List[Card] = field(default_factory=list)
    is_finished: bool = False
    winner_id: Optional[int] = None
    
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
            self.current_player = (self.current_player + 1) % len(self.players)
    
    def get_top_card(self) -> Optional[Card]:
        """Retorna a carta do topo da pilha"""
        if self.pile:
            return self.pile[-1]
        return None
    
    def play_card(self, card: Card):
        """Adiciona uma carta à pilha"""
        self.pile.append(card)

