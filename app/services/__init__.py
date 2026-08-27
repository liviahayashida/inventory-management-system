from app.repositories.produto import ProdutoRepository
from app.repositories.categoria import CategoriaRepository
from app.repositories.fornecedor import FornecedorRepository

from sqlalchemy.orm import Session


class ProdutoService:

    def __init__(self, db: Session):

        self.repository = ProdutoRepository(db)

        self.categoria_repository = CategoriaRepository(db)

        self.fornecedor_repository = FornecedorRepository(db)