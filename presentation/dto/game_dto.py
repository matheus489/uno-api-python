from pydantic import BaseModel
from typing import List
from domain.entities.card import Card, CardColor, CardValue


class CardResponse(BaseModel):
    """DTO para resposta de carta"""
    id: int
    color: str
    value: str
    
    @classmethod
    def from_card(cls, card: Card):
        return cls(
            id=card.id,
            color=card.color.value,
            value=card.value.value
        )


class GameResponse(BaseModel):
    """DTO para resposta de jogo criado"""
    id_jogo: int
    message: str
    players_count: int


class PlayerCardsResponse(BaseModel):
    """DTO para resposta de cartas do jogador"""
    id_jogo: int
    id_jogador: int
    cartas: List[CardResponse]


class CurrentPlayerResponse(BaseModel):
    """DTO para resposta de jogador da vez"""
    id_jogo: int
    id_jogador_da_vez: int


class PlayCardRequest(BaseModel):
    """DTO para requisição de jogada"""
    id_jogo: int
    id_jogador: int
    id_carta: int


class PlayCardResponse(BaseModel):
    """DTO para resposta de jogada"""
    message: str
    won: bool


class PassTurnRequest(BaseModel):
    """DTO para requisição de passar a vez"""
    id_jogo: int
    id_jogador: int


class PassTurnResponse(BaseModel):
    """DTO para resposta de passar a vez"""
    message: str

