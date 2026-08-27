from sqlalchemy.orm import Session

from app.models.fornecedor import Fornecedor
from app.models.produto import Produto
from app.schemas.fornecedor import FornecedorCreate, FornecedorUpdate


class FornecedorRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, apenas_ativos: bool = True):
        query = self.db.query(Fornecedor)

        if apenas_ativos:
            query = query.filter(Fornecedor.ativo.is_(True))

        return query.all()

    def get_by_id(self, fornecedor_id: int):
        return self.db.query(Fornecedor).filter(
            Fornecedor.id == fornecedor_id
        ).first()

    def get_active_by_id(self, fornecedor_id: int):
        return self.db.query(Fornecedor).filter(
            Fornecedor.id == fornecedor_id,
            Fornecedor.ativo.is_(True)
        ).first()

    def get_by_cnpj(self, cnpj: str):
        return self.db.query(Fornecedor).filter(
            Fornecedor.cnpj == cnpj
        ).first()

    def create(self, fornecedor_data: FornecedorCreate):
        fornecedor = Fornecedor(
            razao_social=fornecedor_data.razao_social,
            email=fornecedor_data.email,
            telefone=fornecedor_data.telefone,
            cnpj=fornecedor_data.cnpj
        )

        self.db.add(fornecedor)
        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor

    def update(
        self,
        fornecedor: Fornecedor,
        fornecedor_data: FornecedorUpdate
    ):
        dados = fornecedor_data.model_dump(exclude_unset=True)

        for campo, valor in dados.items():
            setattr(fornecedor, campo, valor)

        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor

    def possui_produtos(self, fornecedor_id: int):
        return self.db.query(Produto).filter(
            Produto.fornecedor_id == fornecedor_id
        ).first() is not None

    def delete(self, fornecedor: Fornecedor):
        fornecedor.ativo = False

        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor