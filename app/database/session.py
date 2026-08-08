from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


DATABASE_URL = ( #gera url (endereço completo para sqlalchemy usar para se conectar com o bd)
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
#     f"mysql+pymysql://{DB_USER}:{senha_segura}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )


engine = create_engine(DATABASE_URL) #cria o motor de conexão com o bd

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
) #conversa temporária com o bd

def get_db():
    db = SessionLocal() #abre uma conversa com o bd

    try:
        yield db #entrega o banco para a função que chamou o get_db(função endpoint, nesse caso)
    finally:
        db.close() #fecha conexão, evita vaza

# try:
#     with engine.connect() as connection:
#         print("✅ Banco conectado com sucesso!")
# except Exception as e:
#     print(f"❌ Erro ao conectar: {e}")

