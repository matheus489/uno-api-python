# Jogo UNO - API FastAPI

API para jogo UNO implementada com FastAPI, seguindo os princípios SOLID e Clean Architecture.

## Estrutura do Projeto

O projeto está organizado em camadas seguindo Clean Architecture:

```
.
├── domain/           # Camada de Domínio (Regras de negócio puras)
│   ├── entities/     # Entidades do domínio (Card, Game, Player)
│   └── repositories/ # Interfaces de repositórios
├── application/      # Camada de Aplicação (Casos de uso)
│   ├── use_cases/    # Casos de uso da aplicação
│   └── services/     # Serviços de aplicação
├── infrastructure/   # Camada de Infraestrutura (Implementações)
│   └── repositories/ # Implementação dos repositórios
├── presentation/     # Camada de Apresentação (API)
│   ├── dto/          # Data Transfer Objects
│   ├── dependencies/ # Container de dependências
│   └── routes/       # Rotas da API
└── main.py          # Ponto de entrada da aplicação
```

## Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
python main.py
```

Ou usando uvicorn diretamente:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em: `http://localhost:8000`

### 3. Documentação da API

Acesse a documentação interativa em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Rotas da API

### 1. Criar Novo Jogo

**GET** `/novoJogo?num_jogadores={numero}`

Inicia um novo jogo com o número especificado de jogadores.

**Exemplo:**
```
GET /novoJogo?num_jogadores=3
```

**Resposta:**
```json
{
  "id_jogo": 1,
  "message": "Jogo criado com sucesso!",
  "players_count": 3
}
```

### 2. Ver Cartas do Jogador

**GET** `/jogo/{id_jogo}/{id_jogador}`

Retorna as cartas na mão de um jogador específico.

**Exemplo:**
```
GET /jogo/1/0
```

**Resposta:**
```json
{
  "id_jogo": 1,
  "id_jogador": 0,
  "cartas": [
    {
      "id": 1,
      "color": "vermelho",
      "value": "5"
    },
    {
      "id": 2,
      "color": "azul",
      "value": "3"
    }
  ]
}
```

### 3. Ver Jogador da Vez

**GET** `/jogo/{id_jogo}/jogado_da_vez`

Retorna o ID do jogador da vez.

**Exemplo:**
```
GET /jogo/1/jogado_da_vez
```

**Resposta:**
```json
{
  "id_jogo": 1,
  "id_jogador_da_vez": 0
}
```

### 4. Jogar uma Carta

**PUT** `/jogo/{id_jogo}/jogar?id_jogador={id}&id_carta={indice}`

Joga uma carta da mão do jogador.

**Exemplo:**
```
PUT /jogo/1/jogar?id_jogador=0&id_carta=0
```

**Resposta:**
```json
{
  "message": "Carta jogada com sucesso",
  "won": false
}
```

Se o jogador ganhar:
```json
{
  "message": "Você ganhou o jogo!",
  "won": true
}
```

### 5. Passar a Vez

**PUT** `/jogo/{id_jogo}/passa?id_jogador={id}`

Passa a vez do jogador, adicionando uma carta à sua mão.

**Exemplo:**
```
PUT /jogo/1/passa?id_jogador=0
```

**Resposta:**
```json
{
  "message": "Vez passada. Uma carta foi adicionada à sua mão."
}
```

## Regras do Jogo

- Cada jogador recebe 5 cartas no início do jogo
- A ordem de jogadas é sempre: jogador 0, jogador 1, jogador 2...
- Uma carta pode ser jogada se:
  - For da mesma cor da carta do topo, OU
  - For do mesmo valor da carta do topo, OU
  - For uma carta coringa
- Se o jogador ficar sem cartas, ele vence o jogo
- Ao passar a vez, o jogador recebe uma carta adicional

## Princípios SOLID Aplicados

### Single Responsibility Principle (SRP)
- Cada classe tem uma única responsabilidade
- `DeckService`: responsável apenas por gerenciar o baralho
- `CreateGameUseCase`: responsável apenas por criar jogos
- Cada caso de uso tem uma responsabilidade específica

### Open/Closed Principle (OCP)
- As interfaces de repositórios permitem extensão sem modificação
- Novos repositórios podem ser criados (ex: `DatabaseGameRepository`) sem alterar o código existente

### Liskov Substitution Principle (LSP)
- Qualquer implementação de `GameRepository` pode ser substituída sem quebrar o código

### Interface Segregation Principle (ISP)
- Interfaces específicas e focadas (como `GameRepository`)

### Dependency Inversion Principle (DIP)
- As camadas superiores dependem de abstrações (interfaces)
- A implementação concreta está na camada de infraestrutura

## Clean Architecture

### Camada de Domínio (domain)
- Entidades puras sem dependências externas
- Interfaces de repositórios

### Camada de Aplicação (application)
- Casos de uso (orquestram as regras de negócio)
- Serviços de domínio

### Camada de Infraestrutura (infrastructure)
- Implementação concreta dos repositórios
- Pode incluir: banco de dados, APIs externas, etc.

### Camada de Apresentação (presentation)
- DTOs para comunicação com o cliente
- Rotas da API
- Container de dependências

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI

## Autor

Implementado seguindo a arquitetura do repositório: [FastAPI-The-Complete-Course](https://github.com/codingwithroby/FastAPI-The-Complete-Course)

