from sqlalchemy import Column, Integer, String
from app.database import Base

class Teste(Base): #CREATE TABLE teste
    __tablename__ = "teste"

    id=Column(Integer, primary_key=True) #id INT PRIMARY KEY
    nome=Column(String(50)) #nome VARCHAR(50)