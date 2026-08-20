from sqlalchemy import Column, DateTime, Integer, Boolean, String, func
from sqlalchemy.orm import relationship

from app.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    ativo = Column(Boolean, default=True, nullable=False)

    produtos = relationship(
        "Produto",
        back_populates="categoria"
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