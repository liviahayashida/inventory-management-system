from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Boolean,
    String,
    Numeric,
    ForeignKey,
    func
)
from sqlalchemy.orm import relationship

from app.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Numeric(10, 2), nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=True
    )

    categoria = relationship(
        "Categoria",
        back_populates="produtos"
    )

    fornecedor_id = Column(
        Integer, ForeignKey("fornecedores.id"), nullable=True
    )

    fornecedor = relationship(
        "Fornecedor", back_populates="produtos"
    )

    criado_em = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    atualizado_em = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )