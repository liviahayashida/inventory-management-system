from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.categoria import CategoriaRepository
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate


class CategoriaService:

    def __init__(self, db: Session):
        self.repository = CategoriaRepository(db)

    def listar(self):
        return self.repository.get_all()

    def buscar_por_id(self, categoria_id: int):
        categoria = self.repository.get_active_by_id(categoria_id)

        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Categoria não encontrada."
            )

        return categoria

    def criar(self, categoria_data: CategoriaCreate):
        categoria_existente = self.repository.get_by_nome(
            categoria_data.nome
        )

        if categoria_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe uma categoria com esse nome."
            )

        return self.repository.create(categoria_data)

    def atualizar(
        self,
        categoria_id: int,
        categoria_data: CategoriaUpdate
    ):
        categoria = self.repository.get_active_by_id(categoria_id)

        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Categoria não encontrada."
            )

        if categoria_data.nome is not None:
            categoria_existente = self.repository.get_by_nome(
                categoria_data.nome
            )

            if (
                categoria_existente
                and categoria_existente.id != categoria_id
            ):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Já existe uma categoria com esse nome."
                )

        return self.repository.update(categoria, categoria_data)

    def excluir(self, categoria_id: int):
        categoria = self.repository.get_active_by_id(categoria_id)

        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Categoria não encontrada."
            )

        if self.repository.possui_produtos(categoria_id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Não é possível excluir uma categoria que possui produtos."
            )

        return self.repository.delete(categoria)