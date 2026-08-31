from sqlalchemy import( Column, DateTime, Integer, String, ForeignKey, func)

from sqlalchemy.orm import relationship
from app.database import Base

class Estoque(Base):
    __tablename__="estoques"
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False, unique=True)
    quantidade_atual=Column(Integer, nullable=False, default=0)
    quantidade_minima=Column(Integer, nullable=False, default=0)
    localizacao=Column(String(100), nullable=True)

    produto = relationship(
    "Produto",
    back_populates="estoque")

    @property
    def estoque_baixo(self):
        return self.quantidade_atual <= self.quantidade_minima

    criado_em = Column(DateTime, server_default=func.now(), nullable=False)

    atualizado_em=Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

