from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.estoque import EstoqueRepository
from app.repositories.produto import ProdutoRepository

from app.schemas.estoque import(EstoqueCreate, EstoqueUpdate, EstoqueQuantidadeUpdate)

class EstoqueService:
    def __init__(self, db: Session):
        self.repository = EstoqueRepository(db)
        self.produto_repository = ProdutoRepository(db)

    def listar(self):
        return self.repository.get_all()

    def buscar_por_id(self, estoque_id: int):
        estoque = self.repository.get_by_id(estoque_id)

        if not estoque:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estoque não encontrado"
            )
        return estoque

    def criar(self, estoque_data: EstoqueCreate):
        produto =self.produto_repository.get_active_by_id(estoque_data.produto_id)

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado ou está inativo."
            )
        estoque_existente = self.repository.get_by_produto_id(
            estoque_data.produto_id
        )

        if estoque_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Este produto já possui um estoque."
            )

        return self.repository.create(estoque_data)

    def atualizar(
        self,
        estoque_id: int,
        estoque_data: EstoqueUpdate
    ):
        estoque = self.repository.get_by_id(estoque_id)

        if not estoque:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estoque não encontrado."
            )

        produto = estoque.produto

        if not produto.ativo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Não é possível alterar o estoque "
                    "de um produto inativo."
                )
            )

        return self.repository.update(estoque, estoque_data)

    def atualizar_quantidade(
        self,
        estoque_id: int,
        estoque_data: EstoqueQuantidadeUpdate
    ):
        estoque = self.repository.get_by_id(estoque_id)

        if not estoque:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estoque não encontrado."
            )

        produto = estoque.produto

        if not produto.ativo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Não é possível alterar o estoque "
                    "de um produto inativo."
                )
            )

        return self.repository.update_quantidade(
            estoque,
            estoque_data
        )