from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from app.repositories.fornecedor import FornecedorRepository
from app.schemas.fornecedor import FornecedorCreate, FornecedorUpdate


class FornecedorService:

    def __init__(self, db: Session):
        self.repository = FornecedorRepository(db)

    def listar(self):
        return self.repository.get_all()

    def buscar_por_id(self, fornecedor_id: int):
        fornecedor = self.repository.get_active_by_id(
            fornecedor_id
        )

        if not fornecedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Fornecedor não encontrado."
            )

        return fornecedor

    def criar(self, fornecedor_data: FornecedorCreate):
        fornecedor_existente = self.repository.get_by_cnpj(
            fornecedor_data.cnpj
        )

        if fornecedor_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um fornecedor com esse CNPJ."
            )

        return self.repository.create(fornecedor_data)

    def atualizar(
        self,
        fornecedor_id: int,
        fornecedor_data: FornecedorUpdate
    ):
        fornecedor = self.repository.get_active_by_id(
            fornecedor_id
        )

        if not fornecedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Fornecedor não encontrado."
            )

        if fornecedor_data.cnpj is not None:
            fornecedor_existente = self.repository.get_by_cnpj(
                fornecedor_data.cnpj
            )

            if (
                fornecedor_existente
                and fornecedor_existente.id != fornecedor_id
            ):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Já existe um fornecedor com esse CNPJ."
                )

        return self.repository.update(
            fornecedor,
            fornecedor_data
        )

    def excluir(self, fornecedor_id: int):
        fornecedor = self.repository.get_active_by_id(
            fornecedor_id
        )

        if not fornecedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Fornecedor não encontrado."
            )

        if self.repository.possui_produtos(fornecedor_id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Não é possível excluir um fornecedor "
                    "que possui produtos."
                )
            )

        return self.repository.delete(fornecedor)