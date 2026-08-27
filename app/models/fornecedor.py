from sqlalchemy import Column, DateTime, Integer, Boolean, String, func
from sqlalchemy.orm import relationship

from app.database import Base

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column (Integer, primary_key=True, index=True)

    razao_social = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False
    )

    telefone=Column(
        String(20),
        nullable=True
    )

    cnpj=Column(
        String(14),
        nullable=False,
        unique=True,
        index=True
    )

    ativo=Column(
        Boolean,
        default=True,
        nullable=False
    )

    produtos = relationship(
        "Produto",
        back_populates="fornecedor"
    )

    criado_em=Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    atualizado_em=Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )