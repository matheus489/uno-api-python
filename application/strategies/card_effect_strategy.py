from abc import ABC, abstractmethod
from domain.entities.game import Game
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.entities.card import CardValue

class CardEffectStrategy(ABC):
    """INterface para estratégias de efeito de cartas"""

    @abstractmethod
    def apply(self, game: Game, facade: CardInteractionFacade):
        """Aplica o efeito da carta no jogo"""
        pass

class NormalStrategy(CardEffectStrategy):
    def apply(self, game: Game, facade: CardInteractionFacade):
        game.next_player()

class SkipStrategy(CardEffectStrategy):
    def apply(self, game: Game, facade: CardInteractionFacade):
        game.next_player()
        game.next_player()

class ReverseStrategy(CardEffectStrategy):
    def apply(self, game: Game, facade: CardInteractionFacade):
        # Se tiver só 2 jogadores, o reverse age como um skip
        if len(game.players) == 2:
            game.next_player()
            game.next_player()
        else:
            game.reverse_direction()
            game.next_player()

class DrawTwoStrategy(CardEffectStrategy):
    def apply(self, game: Game, facade: CardInteractionFacade):
        victim_index = (game.current_player + game.direction) % len(game.players)
        victim_player = game.get_player(victim_index)

        # Compra 2
        for _ in range(2):
            drawn_card = facade.draw_card(game.deck, game.discard_pile)
            victim_player.hand.add_card(drawn_card)
        
        # Perde a vez
        game.next_player()
        game.next_player()



