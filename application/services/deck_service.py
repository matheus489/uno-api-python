from typing import List
from domain.entities.card import Card, CardColor, CardValue


class DeckService:
    """Serviço responsável pela criação e gerenciamento do baralho"""
    
    @staticmethod
    def create_deck() -> List[Card]:
        """Cria um baralho completo do UNO"""
        deck = []
        card_id = 0
        
        # Cores normais (vermelho, azul, verde, amarelo)
        colors = [CardColor.RED, CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW]
        
        for color in colors:
            # Uma carta de valor 0
            deck.append(Card(id=card_id, color=color, value=CardValue.ZERO))
            card_id += 1
            
            # Duas cartas de cada número (1-9)
            for value in [CardValue.ONE, CardValue.TWO, CardValue.THREE, CardValue.FOUR,
                         CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE]:
                deck.append(Card(id=card_id, color=color, value=value))
                card_id += 1
                deck.append(Card(id=card_id, color=color, value=value))
                card_id += 1
            
            # Duas cartas de cada ação
            for value in [CardValue.SKIP, CardValue.REVERSE, CardValue.DRAW_TWO]:
                deck.append(Card(id=card_id, color=color, value=value))
                card_id += 1
                deck.append(Card(id=card_id, color=color, value=value))
                card_id += 1
        
        # Cartas coringa
        for _ in range(4):
            deck.append(Card(id=card_id, color=CardColor.WILD, value=CardValue.WILD))
            card_id += 1
        
        for _ in range(4):
            deck.append(Card(id=card_id, color=CardColor.WILD, value=CardValue.WILD_DRAW_FOUR))
            card_id += 1
        
        return deck
    
    @staticmethod
    def shuffle(deck: List[Card]):
        """Embaralha o baralho"""
        import random
        random.shuffle(deck)
    
    @staticmethod
    def deal_cards(deck: List[Card], num_players: int, cards_per_player: int = 5) -> List[List[Card]]:
        """Distribui cartas para os jogadores"""
        hands = [[] for _ in range(num_players)]
        
        for i in range(cards_per_player):
            for player in range(num_players):
                if deck:
                    hands[player].append(deck.pop())
        
        return hands

