from sqlalchemy import text
from fastapi import APIRouter, Depends

from app.database.session import get_db

router = APIRouter()


@router.get("/health")
def health_check(db=Depends(get_db)):

    try:
        db.execute(text("SELECT 1"))  #     Executa uma consulta simples para verificar a conexão com o banco de dados 
        return {
        "status": "ok",
        "database": "connected"
    }
    except Exception as e:

        return{
        "status": "error",
        "database": "disconnected",
        "error": str(e)
    }