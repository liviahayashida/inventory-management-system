from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.produto import ProdutoRepository
from app.schemas import produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate


class ProdutoService:

    def __init__(self, db: Session):
        self.repository = ProdutoRepository(db)

    def listar(self):
        return self.repository.get_all()

    def buscar_por_id(self, produto_id: int):
        produto = self.repository.get_active_by_id(produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado."
            )

        return produto

    def criar(self, produto_data: ProdutoCreate):
        return self.repository.create(produto_data)

    def atualizar(
        self,
        produto_id: int,
        produto_data: ProdutoUpdate
    ):
        produto = self.repository.get_by_id(produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado."
            )

        if not produto.ativo:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Não é possível atualizar um produto inativo."
            )

        return self.repository.update(produto, produto_data)

    def remover(self, produto_id: int):
        produto = self.repository.get_by_id(produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado."
            )

        if not produto.ativo:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Produto já está inativo."
            )

        return self.repository.delete(produto)
