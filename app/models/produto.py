from sqlalchemy import Column, DateTime, Integer, Boolean, String, Numeric, func
from app.database import Base

class Produto(Base): 
    __tablename__="produtos"

    id=Column(Integer, primary_key=True, index=True)
    nome=Column(String(100), nullable=False)
    descricao=Column(String(255), nullable=True)
    preco=Column(Numeric(10,2), nullable=False)
    ativo=Column(Boolean, default=True, nullable=False)
    # criado_em=Column(DateTime, nullable=False)
    # atualizado_em=Column(DateTime, nullable=False)
    
    criado_em = Column(DateTime, server_default=func.now(), nullable=False)
    atualizado_em = Column(
    DateTime,
    server_default=func.now(),
    onupdate=func.now(),
    nullable=False
)
