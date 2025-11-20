from fastapi import APIRouter, HTTPException, Query
from presentation.dependencies.container import container
from presentation.dto.game_dto import (
    GameResponse, PlayerCardsResponse, CurrentPlayerResponse,
    CardResponse, PlayCardResponse, PassTurnResponse, DrawCardResponse
)
from application.observers.GameStatsObserver import GameStatsObserver


router = APIRouter()

stats_observer = GameStatsObserver()


@router.get("/novoJogo", response_model=GameResponse)
def criar_novo_jogo(num_jogadores: int = Query(..., description="Número de jogadores")):
    """
    Cria um novo jogo UNO.
    
    Args:
        num_jogadores: Número de jogadores que vão jogar
        
    Returns:
        ID do jogo criado
    """
    try:
        print(num_jogadores)
        use_case = container.get_create_game_use_case()
        game = use_case.execute(num_jogadores)
        
        return GameResponse(
            id_jogo=game.id,
            message="Jogo criado com sucesso!",
            players_count=len(game.players)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar jogo: {str(e)}")


@router.get("/jogo", response_model=PlayerCardsResponse)
def ver_cartas_jogador(
    id_jogo: int = Query(..., description="ID do jogo"),
    id_jogador: int = Query(..., description="ID do jogador")):
    """
    Retorna as cartas de um jogador específico.
    
    Args:
        id_jogo: ID do jogo
        id_jogador: ID do jogador
        
    Returns:
        Lista de cartas do jogador
    """
    try:
        use_case = container.get_get_player_cards_use_case()
        cards = use_case.execute(id_jogo, id_jogador)
        
        return PlayerCardsResponse(
            id_jogo=id_jogo,
            id_jogador=id_jogador,
            cartas=[CardResponse.from_card(card) for card in cards]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar cartas: {str(e)}")


@router.get("/jogo/{id_jogo}/jogador_da_vez", response_model=CurrentPlayerResponse)
def ver_jogador_da_vez(id_jogo: int):
    """
    Retorna o ID do jogador da vez.
    
    Args:
        id_jogo: ID do jogo
        
    Returns:
        ID do jogador da vez
    """
    try:
        use_case = container.get_get_current_player_use_case()
        current_player_id = use_case.execute(id_jogo)
        
        return CurrentPlayerResponse(
            id_jogo=id_jogo,
            id_jogador_da_vez=current_player_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar jogador da vez: {str(e)}")
    

@router.get("/stats", response_model=dict)
def get_game_stats():
    """
    Retorna estatísticas do jogo.
    """
    return stats_observer.get_stats()

@router.put("/jogo/{id_jogo}/jogar", response_model=PlayCardResponse)
def jogar_carta(
    id_jogo: int,
    id_jogador: int = Query(..., description="ID do jogador"),
    id_carta: int = Query(..., description="Índice da carta na mão do jogador")
):
    """
    Joga uma carta de um jogador.
    
    Args:
        id_jogo: ID do jogo
        id_jogador: ID do jogador
        id_carta: Índice da carta na mão do jogador
        
    Returns:
        Mensagem de sucesso ou erro
    """
    try:
        use_case = container.get_play_card_use_case()
        use_case.attach_observer(stats_observer)

        result = use_case.execute(id_jogo, id_jogador, id_carta)

        return PlayCardResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao jogar carta: {str(e)}")


@router.put("/jogo/{id_jogo}/passa", response_model=PassTurnResponse)
def passar_vez(
    id_jogo: int,
    id_jogador: int = Query(..., description="ID do jogador")
):
    """
    Passa a vez do jogador, adicionando uma carta à sua mão.
    
    Args:
        id_jogo: ID do jogo
        id_jogador: ID do jogador
        
    Returns:
        Mensagem de confirmação
    """
    try:
        use_case = container.get_pass_turn_use_case()
        result = use_case.execute(id_jogo, id_jogador)
        
        return PassTurnResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao passar a vez: {str(e)}")

@router.put("/jogo/{id_jogo}/puxar_carta", response_model=DrawCardResponse)
def puxar_carta(
    id_jogo: int,
    id_jogador: int = Query(..., description="ID do jogador")
):
    """
    Puxa uma carta do baralho para o jogador.
    
    Args:
        id_jogo: ID do jogo
        id_jogador: ID do jogador
        
    Returns:
        Mensagem de confirmação
    """
    try:
        use_case = container.put_draw_card_use_case()
        result = use_case.execute(id_jogo, id_jogador)
        
        return DrawCardResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao puxar carta: {str(e)}")

@router.get("/jogo/carta_do_topo", response_model=CardResponse)
def ver_carta_do_topo(id_jogo: int = Query(..., description="ID do jogo")):
    """
    Retorna a carta do topo da pilha de descarte.
    
    Args:
        id_jogo: ID do jogo
        
    Returns:
        Carta do topo da pilha de descarte
    """
    try:
        use_case = container.get_top_card_use_case()
        top_card = use_case.execute(id_jogo)
        
        return CardResponse.from_card(top_card)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar carta do topo: {str(e)}")