from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CategoriaCreate(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    descricao: str | None = Field(default=None, max_length=255)


class CategoriaUpdate(BaseModel):
    nome: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    descricao: str | None = Field(
        default=None,
        max_length=255
    )

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

        return values


class CategoriaResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes=True)