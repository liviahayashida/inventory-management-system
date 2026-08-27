from fastapi import FastAPI
from app.routers import produto, categoria, fornecedor
import app.database.session
from app.api.routes.health import router as health_router

app = FastAPI(
    title="Inventory Management System API",
    description="REST API for inventory management built with FastAPI.",
    version="1.0.0",
)#cria a aplicação
app.include_router(produto.router)
app.include_router(categoria.router)
app.include_router(fornecedor.router)
app.include_router(health_router)

@app.get("/") #executa isso quando a rota raiz for acessada
def root(): #função python (responde a uma requisição HTTP GET)
    return{
        "message" : "Hello World, Inventory Management System API"
    } #FastAPI converte para json automaticamente