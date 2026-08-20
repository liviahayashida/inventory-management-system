from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.categoria import (
    CategoriaCreate,
    CategoriaUpdate,
    CategoriaResponse
)
from app.services.categoria import CategoriaService


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


@router.get(
    "/",
    response_model=list[CategoriaResponse],
    status_code=status.HTTP_200_OK
)
def listar_categorias(db: Session = Depends(get_db)):
    service = CategoriaService(db)
    return service.listar()


@router.get(
    "/{categoria_id}",
    response_model=CategoriaResponse,
    status_code=status.HTTP_200_OK
)
def buscar_categoria(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    service = CategoriaService(db)
    return service.buscar_por_id(categoria_id)


@router.post(
    "/",
    response_model=CategoriaResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_categoria(
    categoria_data: CategoriaCreate,
    db: Session = Depends(get_db)
):
    service = CategoriaService(db)
    return service.criar(categoria_data)


@router.put(
    "/{categoria_id}",
    response_model=CategoriaResponse,
    status_code=status.HTTP_200_OK
)
def atualizar_categoria(
    categoria_id: int,
    categoria_data: CategoriaUpdate,
    db: Session = Depends(get_db)
):
    service = CategoriaService(db)
    return service.atualizar(categoria_id, categoria_data)


@router.delete(
    "/{categoria_id}",
    response_model=CategoriaResponse,
    status_code=status.HTTP_200_OK
)
def excluir_categoria(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    service = CategoriaService(db)
    return service.excluir(categoria_id)