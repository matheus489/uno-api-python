from fastapi import FastAPI
from presentation.routes import game_routes

app = FastAPI(
    title="UNO Game API",
    description="API para jogo UNO com FastAPI e Clean Architecture",
    version="1.0.0"
)

# Registra as rotas
app.include_router(game_routes.router)


@app.get("/")
def root():
    """Endpoint raiz"""
    return {"message": "Bem-vindo à API do Jogo UNO!", "version": "1.0.0"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
