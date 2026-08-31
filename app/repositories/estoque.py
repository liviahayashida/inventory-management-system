from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.schemas.estoque import (EstoqueCreate, EstoqueUpdate, EstoqueQuantidadeUpdate)

class EstoqueRepository:

    def __init__(self, db: Session):
        self.db= db

    def get_all(self):
        return self.db.query(Estoque).all()

    def get_by_id(self, estoque_id: int):
        return self.db.query(Estoque).filter(
            Estoque.id==estoque_id).first()

    def get_by_produto_id(self, produto_id: int):
        return self.db.query(Estoque).filter(
            Estoque.produto_id == produto_id
        ).first()

    def create(self, estoque_data: EstoqueCreate):
        estoque = Estoque(
            produto_id=estoque_data.produto_id,
            quantidade_minima=estoque_data.quantidade_minima,
            localizacao=estoque_data.localizacao
        )

        self.db.add(estoque)
        self.db.commit()
        self.db.refresh(estoque)

        return estoque

    def update(self, estoque: Estoque, estoque_data: EstoqueUpdate):
        dados = estoque_data.model_dump(exclude_unset=True)

        for campo, valor in dados.items():
            setattr(estoque, campo, valor)

        self.db.commit()
        self.db.refresh(estoque)

        return estoque

    def update_quantidade(
        self,
        estoque: Estoque,
        estoque_data: EstoqueQuantidadeUpdate
    ):
        estoque.quantidade_atual = estoque_data.quantidade_atual
 
        self.db.commit()
        self.db.refresh(estoque)

        return estoque