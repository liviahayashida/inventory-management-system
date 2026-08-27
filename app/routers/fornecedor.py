from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.fornecedor import (
    FornecedorCreate,
    FornecedorUpdate,
    FornecedorResponse
)

from app.services.fornecedor import FornecedorService


router = APIRouter(
    prefix="/fornecedores",
    tags=["Fornecedores"]
)


@router.get(
    "/",
    response_model=list[FornecedorResponse],
    status_code=status.HTTP_200_OK
)
def listar_fornecedores(
    db: Session = Depends(get_db)
):
    service = FornecedorService(db)

    return service.listar()


@router.get(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    status_code=status.HTTP_200_OK
)
def buscar_fornecedor(
    fornecedor_id: int,
    db: Session = Depends(get_db)
):
    service = FornecedorService(db)

    return service.buscar_por_id(fornecedor_id)


@router.post(
    "/",
    response_model=FornecedorResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_fornecedor(
    fornecedor_data: FornecedorCreate,
    db: Session = Depends(get_db)
):
    service = FornecedorService(db)

    return service.criar(fornecedor_data)


@router.put(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    status_code=status.HTTP_200_OK
)
def atualizar_fornecedor(
    fornecedor_id: int,
    fornecedor_data: FornecedorUpdate,
    db: Session = Depends(get_db)
):
    service = FornecedorService(db)

    return service.atualizar(
        fornecedor_id,
        fornecedor_data
    )


@router.delete(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    status_code=status.HTTP_200_OK
)
def excluir_fornecedor(
    fornecedor_id: int,
    db: Session = Depends(get_db)
):
    service = FornecedorService(db)

    return service.excluir(fornecedor_id)