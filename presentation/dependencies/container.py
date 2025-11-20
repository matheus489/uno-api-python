"""Container de dependências para injeção no FastAPI"""
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.facades.CardInteractionFacade import CardInteractionFacade
from application.observers.GameStatsObserver import GameStatsObserver
from application.use_cases.create_game import CreateGameUseCase
from application.use_cases.get_player_cards import GetPlayerCardsUseCase
from application.use_cases.get_current_player import GetCurrentPlayerUseCase
from application.use_cases.play_card import PlayCardUseCase
from application.use_cases.pass_turn import PassTurnUseCase
from application.use_cases.draw_card import DrawCardUseCase
from application.use_cases.top_card import TopCardUseCase


class Container:
    """Container de dependências"""
    
    def __init__(self):
        # Repositório
        self.game_repository = InMemoryGameRepository()
        self.card_facade = CardInteractionFacade()
        self.stats_observer = GameStatsObserver()
        
        # Casos de uso
        self.create_game_use_case = CreateGameUseCase(
            self.game_repository, 
            self.card_facade
        )

        self.get_player_cards_use_case = GetPlayerCardsUseCase(self.game_repository)

        self.get_current_player_use_case = GetCurrentPlayerUseCase(self.game_repository)

        self.play_card_use_case = PlayCardUseCase(
            self.game_repository,
            self.card_facade
        )

        self.pass_turn_use_case = PassTurnUseCase(self.game_repository)

        self.draw_card_use_case = DrawCardUseCase(
            self.game_repository,
            self.card_facade
        )

        self.top_card_use_case = TopCardUseCase(
            self.game_repository,
            self.card_facade
        )
    
    def get_create_game_use_case(self) -> CreateGameUseCase:
        return self.create_game_use_case
    
    def get_get_player_cards_use_case(self) -> GetPlayerCardsUseCase:
        return self.get_player_cards_use_case
    
    def get_get_current_player_use_case(self) -> GetCurrentPlayerUseCase:
        return self.get_current_player_use_case
    
    def get_play_card_use_case(self) -> PlayCardUseCase:
        return self.play_card_use_case
    
    def get_pass_turn_use_case(self) -> PassTurnUseCase:
        return self.pass_turn_use_case
    
    def put_draw_card_use_case(self) -> DrawCardUseCase:
        return self.draw_card_use_case
    
    def get_top_card_use_case(self) -> TopCardUseCase:
        return self.top_card_use_case


# Instância global do container
container = Container()

