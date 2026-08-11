from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.produto import (
    ProdutoCreate,
    ProdutoUpdate,
    ProdutoResponse
)

from app.services.produto import ProdutoService
#criando o router
router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

#primeiro endpoint
@router.get(
    "",
    response_model=list[ProdutoResponse]
)
def listar_produtos(
    db: Session = Depends(get_db)
):
    service = ProdutoService(db)

    return service.listar()

#get
@router.get(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    service = ProdutoService(db)

    return service.buscar_por_id(produto_id)

#post
@router.post(
    "",
    response_model=ProdutoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_produto(
    produto_data: ProdutoCreate,
    db: Session = Depends(get_db)
):
    service = ProdutoService(db)

    return service.criar(produto_data)

#PUT
@router.put(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def atualizar_produto(
    produto_id: int,
    produto_data: ProdutoUpdate,
    db: Session = Depends(get_db)
):
    service = ProdutoService(db)

    return service.atualizar(
        produto_id,
        produto_data
    )

#delete
@router.delete(
    "/{produto_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remover_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    service = ProdutoService(db)

    service.remover(produto_id)
