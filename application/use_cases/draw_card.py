from application.facades.CardInteractionFacade import CardInteractionFacade
from domain.repositories.game_repository import GameRepository
from domain.entities.card import Card

class DrawCardUseCase:

    def __init__(self, game_repository: GameRepository, card_facade: CardInteractionFacade ):
        self.game_repository = game_repository
        self.card_facade = card_facade

    def execute(self, game_id: int, player_id: int) -> Card:
        # Buscar o jogo
        game = self.game_repository.find_by_id(game_id)
        if not game:
            raise ValueError(f"Jogo com ID {game_id} não encontrado.")
        
        # Verifica se é o jogador da vez
        if game.current_player != player_id:
            raise ValueError(f"Não é a vez do jogador {player_id}. Jogador da vez: {game.current_player}")

        # Buscar o jogador
        player = game.get_player(player_id)
        if not player:
            raise ValueError(f"Jogador com ID {player_id} não encontrado no jogo {game_id}.")

        # Puxar uma carta do baralho
        drawn_card = self.card_facade.draw_card(game.deck, game.discard_pile)
        if not drawn_card:
            raise ValueError("Não há cartas suficientes no baralho para puxar.")

        # Adicionar a carta à mão do jogador
        self.card_facade.add_card_to_hand(player.hand, drawn_card)

        return drawn_card


