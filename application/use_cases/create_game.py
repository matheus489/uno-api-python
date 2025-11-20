from domain.entities.game import Game, Player
from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.repositories.game_repository import GameRepository


class CreateGameUseCase:
    """Caso de uso: Criar um novo jogo"""
    
    def __init__(self, game_repository: GameRepository, card_facade: CardInteractionFacade):
        self.game_repository = game_repository
        self.next_game_id = 1
        self.card_facade = card_facade
    
    def execute(self, num_players: int) -> Game:
        """Cria um novo jogo com o número especificado de jogadores"""
        # Validar número de jogadores
        if num_players < 2:
            raise ValueError("É necessário pelo menos 2 jogadores para iniciar um jogo")
        
        # Criar o jogo
        game = Game(id=self.next_game_id)
        self.next_game_id += 1
        
        # Criar o baralho e revelar a primeira carta
        self.card_facade.setup_new_game(game.deck, game.discard_pile)

        
        # Distribuir cartas
        hands = self.card_facade.deal_initial_hands(num_players, game.deck, cards_per_player=7)
        
        # Criar jogadores com suas cartas
        for i in range(num_players):
            player = Player(id=i)
            player.hand = hands[i]
            game.add_player(player)
        
        # Salvar o jogo
        self.game_repository.create(game)
        
        return game

