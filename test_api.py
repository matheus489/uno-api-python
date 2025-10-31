"""
Script de teste para demonstrar o uso da API
"""
import requests

BASE_URL = "http://localhost:8001"

def test_api():
    print("=" * 60)
    print("TESTE DA API DO JOGO UNO")
    print("=" * 60)
    
    # 1. Criar um novo jogo com 3 jogadores
    print("\n1. Criando um novo jogo com 3 jogadores...")
    response = requests.get(f"{BASE_URL}/novoJogo?num_jogadores=3")
    print(f"Status: {response.status_code}")
    game_data = response.json()
    print(f"Resposta: {game_data}")
    game_id = game_data["id_jogo"]
    
    # 2. Ver cartas do jogador 0
    print(f"\n2. Verificando cartas do jogador 0...")
    response = requests.get(f"{BASE_URL}/jogo/{game_id}/0")
    print(f"Status: {response.status_code}")
    cards_data = response.json()
    print(f"Cartas do jogador 0: {[c['color'] + ' ' + c['value'] for c in cards_data['cartas']]}")
    
    # 3. Ver jogador da vez
    print(f"\n3. Verificando jogador da vez...")
    response = requests.get(f"{BASE_URL}/jogo/{game_id}/jogado_da_vez")
    print(f"Status: {response.status_code}")
    current_player = response.json()
    print(f"Jogador da vez: {current_player['id_jogador_da_vez']}")
    
    # 4. Jogar uma carta
    print(f"\n4. Jogador 0 jogando a primeira carta (índice 0)...")
    response = requests.put(f"{BASE_URL}/jogo/{game_id}/jogar?id_jogador=0&id_carta=0")
    print(f"Status: {response.status_code}")
    play_result = response.json()
    print(f"Resultado: {play_result}")
    
    # 5. Verificar jogador da vez novamente
    print(f"\n5. Verificando jogador da vez novamente...")
    response = requests.get(f"{BASE_URL}/jogo/{game_id}/jogado_da_vez")
    print(f"Status: {response.status_code}")
    current_player = response.json()
    print(f"Jogador da vez: {current_player['id_jogador_da_vez']}")
    
    # 6. Ver cartas do jogador 0 após jogar
    print(f"\n6. Verificando cartas do jogador 0 após jogar...")
    response = requests.get(f"{BASE_URL}/jogo/{game_id}/0")
    print(f"Status: {response.status_code}")
    cards_data = response.json()
    print(f"Cartas restantes: {len(cards_data['cartas'])}")
    
    print("\n" + "=" * 60)
    print("TESTE CONCLUÍDO!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar à API.")
        print("Certifique-se de que o servidor está rodando em http://localhost:8000")
    except Exception as e:
        print(f"Erro: {e}")
