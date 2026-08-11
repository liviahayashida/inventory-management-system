from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate


class ProdutoRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, apenas_ativos: bool = True):
        query = self.db.query(Produto)

        if apenas_ativos:
            query = query.filter(Produto.ativo.is_(True))

        return query.all()

    def get_by_id(self, produto_id: int):
        return self.db.query(Produto).filter(
            Produto.id == produto_id
        ).first()  # select * from produtos where id=produto_id (nao filtra ativo)
    def get_active_by_id(self, produto_id: int):
        return self.db.query(Produto).filter(
            Produto.id ==produto_id,
            Produto.ativo==True
        ).first()

    def create(self, produto_data: ProdutoCreate):
        produto = Produto(
            nome=produto_data.nome,
            descricao=produto_data.descricao,
            preco=produto_data.preco
        )

        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)  # atualiza o objeto python com os valores reais que estao no banco

        return produto

    def update(self, produto: Produto, produto_data: ProdutoUpdate):
        dados = produto_data.model_dump(exclude_unset=True)

        for campo, valor in dados.items():
            setattr(produto, campo, valor)

        self.db.commit()
        self.db.refresh(produto)

        return produto

    def delete(self, produto: Produto):
        produto.ativo = False

        self.db.commit()
        self.db.refresh(produto)

        return produto
