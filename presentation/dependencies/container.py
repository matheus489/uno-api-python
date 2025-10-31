"""Container de dependências para injeção no FastAPI"""
from infrastructure.repositories.game_repository_impl import InMemoryGameRepository
from application.use_cases.create_game import CreateGameUseCase
from application.use_cases.get_player_cards import GetPlayerCardsUseCase
from application.use_cases.get_current_player import GetCurrentPlayerUseCase
from application.use_cases.play_card import PlayCardUseCase
from application.use_cases.pass_turn import PassTurnUseCase


class Container:
    """Container de dependências"""
    
    def __init__(self):
        # Repositório
        self.game_repository = InMemoryGameRepository()
        
        # Casos de uso
        self.create_game_use_case = CreateGameUseCase(self.game_repository)
        self.get_player_cards_use_case = GetPlayerCardsUseCase(self.game_repository)
        self.get_current_player_use_case = GetCurrentPlayerUseCase(self.game_repository)
        self.play_card_use_case = PlayCardUseCase(self.game_repository)
        self.pass_turn_use_case = PassTurnUseCase(self.game_repository)
    
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


# Instância global do container
container = Container()

