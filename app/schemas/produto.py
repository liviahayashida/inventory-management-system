from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ProdutoCreate(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    descricao: str | None = Field(default=None, max_length=255)
    preco: Decimal = Field(gt=0)


class ProdutoUpdate(BaseModel):
    nome: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    descricao: str | None = Field(
        default=None,
        max_length=255
    )
    preco: Decimal | None = Field(
        default=None,
        gt=0
    )

#atualização precisa ter pelo menos um campo, colocamos uma regra que Field() nao resolveria sozinho
    @model_validator(mode="before")
    @classmethod
    def validar_atualizacao(cls, values):
        if not isinstance(values, dict):
            return values

        if not values:
            raise ValueError(
                "Pelo menos um campo deve ser informado para atualização."
            )

        if "nome" in values and values["nome"] is None:
            raise ValueError("O campo 'nome' não pode ser nulo.")

        if "preco" in values and values["preco"] is None:
            raise ValueError("O campo 'preco' não pode ser nulo.")

        return values

# programa controla nome, descricao e preco do produto, alem de ativo ou n

# Resposta do produto, oq a API vai retornar:
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None
    preco: Decimal
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes=True)