from domain.entities.card import Card
from domain.repositories.game_repository import GameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade

class TopCardUseCase:
    def __init__(self, game_repository: GameRepository, card_facade: CardInteractionFacade):
        self.game_repository = game_repository
        self.card_facade = card_facade

    def execute(self, game_id: int) -> Card:
        game = self.game_repository.find_by_id(game_id)
        top_card = self.card_facade.get_top_card(game.discard_pile)
        if not game:
            raise ValueError("Jogo não encontrado")

        return top_card