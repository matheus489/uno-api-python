from typing import List
from domain.entities.card import Card
from domain.entities.deck import Deck
from domain.entities.pile import Pile
from domain.entities.hand import Hand

# Apenas para ilustrar as estruturas de dados (provavelmente você já tem seus models)

class CardInteractionFacade:
    """
    Fachada para simplificar todas as operações complexas envolvendo cartas,
    baralhos e validações de regras de movimento.
    """

    def setup_new_game(self, deck: Deck, pile: Pile):
        """Cria o baralho, embaralha e vira a primeira carta."""
        deck.create_full_deck()
        deck.shuffle()
        first_card = deck.draw()
        pile.add_card(first_card)
        

    def deal_initial_hands(self, num_players: int, deck: Deck, cards_per_player: int = 7) -> List[List[Card]]:
        """Distribui as mãos iniciais para todos os jogadores."""
        hands = []
        for _ in range(num_players):
            hand = [deck.draw() for _ in range(cards_per_player)]
            hands.append(hand)
        return hands

    def draw_card(self, deck: Deck, pile: Pile) -> Card:
        """
        Saca uma carta. Se o baralho estiver vazio, recicla o descarte.
        """
        if deck.is_empty():
            # Lógica de 'reshuffle': Pega o descarte (menos a topo), embaralha e vira novo deck
            top_card = pile.pop_top_card()
            cards_to_recycle = pile.remove_all()
            deck.add_cards(cards_to_recycle)
            deck.shuffle()
            pile.add_card(top_card)
            
        return deck.draw()

    def validate_move(self, card_played: Card, current_top_card: Card) -> bool:
        """
        Verifica se a jogada é válida segundo as regras do UNO.
        Isso tira a regra de negócio complexa de dentro do Use Case.
        """
        # Regra 1: Mesma cor
        if card_played.color == current_top_card.color:
            return True
        # Regra 2: Mesmo valor/símbolo
        if card_played.value == current_top_card.value:
            return True
        # Regra 3: Carta coringa (Muda cor ou +4)
        # if card_played.color == ColorEnum.BLACK: # Exemplo de coringa
        #     return True
            
        return False

    def play_card(self, card: Card, pile: Pile):
        """Joga a carta na pilha de descarte."""
        pile.add_card(card)

    def add_card_to_hand(self, hand: Hand, card: Card):
        hand.add_card(card)

    def get_top_card(self, pile: Pile) -> Card:
        """Retorna a carta do topo da pilha de descarte."""
        return pile.get_top_card()