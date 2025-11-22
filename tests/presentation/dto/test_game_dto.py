import pytest
from presentation.dto.game_dto import (
    CardResponse, GameResponse, PlayerCardsResponse,
    CurrentPlayerResponse, PlayCardResponse, PassTurnResponse, DrawCardResponse
)
from domain.entities.card import Card, CardColor, CardValue


class TestCardResponse:
    """Testes para CardResponse DTO"""
    
    def test_card_response_from_card(self):
        card = Card(color=CardColor.RED, value=CardValue.ONE, id=1)
        response = CardResponse.from_card(card)
        
        assert response.id == 1
        assert response.color == "vermelho"
        assert response.value == "1"
    
    def test_card_response_creation(self):
        response = CardResponse(id=1, color="azul", value="2")
        
        assert response.id == 1
        assert response.color == "azul"
        assert response.value == "2"


class TestGameResponse:
    """Testes para GameResponse DTO"""
    
    def test_game_response_creation(self):
        response = GameResponse(
            id_jogo=1,
            message="Jogo criado com sucesso!",
            players_count=3
        )
        
        assert response.id_jogo == 1
        assert response.message == "Jogo criado com sucesso!"
        assert response.players_count == 3


class TestPlayerCardsResponse:
    """Testes para PlayerCardsResponse DTO"""
    
    def test_player_cards_response_creation(self):
        card1 = CardResponse(id=1, color="vermelho", value="1")
        card2 = CardResponse(id=2, color="azul", value="2")
        
        response = PlayerCardsResponse(
            id_jogo=1,
            id_jogador=0,
            cartas=[card1, card2]
        )
        
        assert response.id_jogo == 1
        assert response.id_jogador == 0
        assert len(response.cartas) == 2
        assert response.cartas[0] == card1
        assert response.cartas[1] == card2


class TestCurrentPlayerResponse:
    """Testes para CurrentPlayerResponse DTO"""
    
    def test_current_player_response_creation(self):
        response = CurrentPlayerResponse(
            id_jogo=1,
            id_jogador_da_vez=2
        )
        
        assert response.id_jogo == 1
        assert response.id_jogador_da_vez == 2


class TestPlayCardResponse:
    """Testes para PlayCardResponse DTO"""
    
    def test_play_card_response_creation(self):
        response = PlayCardResponse(
            message="Carta jogada com sucesso",
            won=False
        )
        
        assert response.message == "Carta jogada com sucesso"
        assert response.won is False
    
    def test_play_card_response_won(self):
        response = PlayCardResponse(
            message="Você ganhou o jogo!",
            won=True
        )
        
        assert response.message == "Você ganhou o jogo!"
        assert response.won is True


class TestPassTurnResponse:
    """Testes para PassTurnResponse DTO"""
    
    def test_pass_turn_response_creation(self):
        response = PassTurnResponse(
            message="Vez passada. Uma carta foi adicionada à sua mão."
        )
        
        assert response.message == "Vez passada. Uma carta foi adicionada à sua mão."


class TestDrawCardResponse:
    """Testes para DrawCardResponse DTO"""
    
    def test_draw_card_response_creation(self):
        card = CardResponse(id=1, color="verde", value="3")
        response = DrawCardResponse(
            message="Jogador 0 puxou uma carta com sucesso.",
            card=card
        )
        
        assert response.message == "Jogador 0 puxou uma carta com sucesso."
        assert response.card == card

