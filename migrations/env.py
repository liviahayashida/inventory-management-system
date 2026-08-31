import sys
from pathlib import Path
from logging.config import fileConfig

# 1. Garante que a raiz do projeto está no sys.path ANTES de importar a aplicação
sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import engine_from_config, pool
from alembic import context

# 2. Importa a base do banco de dados e as entidades (models)
from app.database import Base
import app.models
from app.database.session import engine

# IMPORTANTE: Todos os seus models precisam ser importados aqui para registrar no Base.metadata
# from app.models.teste import Teste 

# 3. Configuração do Alembic e Metadata
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata #antes desta linha ad models tem q ser importadas


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()