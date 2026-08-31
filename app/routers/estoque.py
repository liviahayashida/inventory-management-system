from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.estoque import (
    EstoqueCreate,
    EstoqueUpdate,
    EstoqueQuantidadeUpdate,
    EstoqueResponse
)

from app.services.estoque import EstoqueService


router = APIRouter(
    prefix="/estoques",
    tags=["Estoques"]
)


@router.get(
    "",
    response_model=list[EstoqueResponse]
)
def listar_estoques(
    db: Session = Depends(get_db)
):
    service = EstoqueService(db)

    return service.listar()


@router.get(
    "/{estoque_id}",
    response_model=EstoqueResponse
)
def buscar_estoque(
    estoque_id: int,
    db: Session = Depends(get_db)
):
    service = EstoqueService(db)

    return service.buscar_por_id(estoque_id)


@router.post(
    "",
    response_model=EstoqueResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_estoque(
    estoque_data: EstoqueCreate,
    db: Session = Depends(get_db)
):
    service = EstoqueService(db)

    return service.criar(estoque_data)


@router.put(
    "/{estoque_id}",
    response_model=EstoqueResponse
)
def atualizar_estoque(
    estoque_id: int,
    estoque_data: EstoqueUpdate,
    db: Session = Depends(get_db)
):
    service = EstoqueService(db)

    return service.atualizar(
        estoque_id,
        estoque_data
    )


@router.put(
    "/{estoque_id}/quantidade",
    response_model=EstoqueResponse
)
def atualizar_quantidade(
    estoque_id: int,
    estoque_data: EstoqueQuantidadeUpdate,
    db: Session = Depends(get_db)
):
    service = EstoqueService(db)

    return service.atualizar_quantidade(
        estoque_id,
        estoque_data
    )