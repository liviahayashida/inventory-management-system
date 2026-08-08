# from logging.config import fileConfig

# from sqlalchemy import engine_from_config
# from sqlalchemy import pool

# from alembic import context
# from app.database import Base
# from app.models import teste
# from app.database.session import engine
# import app.models

# import sys
# from pathlib import Path




# sys.path.append(str(Path(__file__).resolve().parents[1]))

# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config

# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# # target_metadata = mymodel.Base.metadata
# target_metadata = Base.metadata

# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.


# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode.

#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.

#     Calls to context.execute() here emit the given string to the
#     script output.

#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()


# from app.models.teste import Teste
# print("--- CLASSES QUE O ALEMBIC ESTÁ VENDO NO METADATA ---")
# for table_name in Base.metadata.tables:
#     print(f"Tabela encontrada: {table_name}")
# print("--------------------------------------------------")

# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode."""
#     connectable = engine

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, 
#             target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()
# # def run_migrations_online() -> None:
# #     """Run migrations in 'online' mode.

# #     In this scenario we need to create an Engine
# #     and associate a connection with the context.

# #     """
# #     connectable = engine_from_config(
# #         config.get_section(config.config_ini_section, {}),
# #         prefix="sqlalchemy.",
# #         poolclass=pool.NullPool,
# #     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()
import sys
from pathlib import Path
from logging.config import fileConfig

# 1. Garante que a raiz do projeto está no sys.path ANTES de importar a aplicação
sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import engine_from_config, pool
from alembic import context

# 2. Importa a base do banco de dados e as entidades (models)
from app.database import Base
from app.database.session import engine

# IMPORTANTE: Todos os seus models precisam ser importados aqui para registrar no Base.metadata
from app.models.teste import Teste 

# 3. Configuração do Alembic e Metadata
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


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