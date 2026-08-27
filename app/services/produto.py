from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.fornecedor import FornecedorRepository
from app.repositories.produto import ProdutoRepository
from app.repositories.categoria import CategoriaRepository

from app.schemas.produto import ProdutoCreate, ProdutoUpdate

class ProdutoService:

    def __init__(self, db: Session):
        self.repository = ProdutoRepository(db)
        self.categoria_repository = CategoriaRepository(db)
        self.fornecedor_repository = FornecedorRepository(db)

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

        # Valida categoria
        if produto_data.categoria_id is not None:
            categoria = self.categoria_repository.get_active_by_id(
                produto_data.categoria_id
            )

            if not categoria:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Categoria não encontrada ou está inativa."
                )

        # Valida fornecedor
        if produto_data.fornecedor_id is not None:
            fornecedor = self.fornecedor_repository.get_active_by_id(
                produto_data.fornecedor_id
            )

            if not fornecedor:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Fornecedor não encontrado ou está inativo."
                )

        # Cria o produto
        return self.repository.create(produto_data)

    def atualizar(
        self,
        produto_id: int,
        produto_data: ProdutoUpdate
    ):

        produto = self.repository.get_active_by_id(produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado."
            )

        # Valida categoria
        if produto_data.categoria_id is not None:
            categoria = self.categoria_repository.get_active_by_id(
                produto_data.categoria_id
            )

            if not categoria:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Categoria não encontrada ou está inativa."
                )

        # Valida fornecedor
        if produto_data.fornecedor_id is not None:
            fornecedor = self.fornecedor_repository.get_active_by_id(
                produto_data.fornecedor_id
            )

            if not fornecedor:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Fornecedor não encontrado ou está inativo."
                )

        return self.repository.update(produto, produto_data)

    def excluir(self, produto_id: int):

        produto = self.repository.get_active_by_id(produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado."
            )

        return self.repository.delete(produto)
