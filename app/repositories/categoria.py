from sqlalchemy.orm import Session

from app.models.categoria import Categoria
from app.models.produto import Produto
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate


class CategoriaRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, apenas_ativas: bool = True):
        query = self.db.query(Categoria)

        if apenas_ativas:
            query = query.filter(Categoria.ativo.is_(True))

        return query.all()

    def get_by_id(self, categoria_id: int):
        return self.db.query(Categoria).filter(
            Categoria.id == categoria_id
        ).first()

    def get_active_by_id(self, categoria_id: int):
        return self.db.query(Categoria).filter(
            Categoria.id == categoria_id,
            Categoria.ativo.is_(True)
        ).first()

    def get_by_nome(self, nome: str):
        return self.db.query(Categoria).filter(
            Categoria.nome == nome
        ).first()

    def create(self, categoria_data: CategoriaCreate):
        categoria = Categoria(
            nome=categoria_data.nome,
            descricao=categoria_data.descricao
        )

        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)

        return categoria

    def update(
        self,
        categoria: Categoria,
        categoria_data: CategoriaUpdate
    ):
        dados = categoria_data.model_dump(exclude_unset=True)

        for campo, valor in dados.items():
            setattr(categoria, campo, valor)

        self.db.commit()
        self.db.refresh(categoria)

        return categoria

    def possui_produtos(self, categoria_id: int):
        return self.db.query(Produto).filter(
            Produto.categoria_id == categoria_id
        ).first() is not None

    def delete(self, categoria: Categoria):
        categoria.ativo = False

        self.db.commit()
        self.db.refresh(categoria)

        return categoria