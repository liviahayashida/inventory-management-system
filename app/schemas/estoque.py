from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ConfigDict

class EstoqueCreate(BaseModel):
    produto_id: int = Field(...,ge=1)
    quantidade_minima: int = Field(..., ge=0)
    localizacao: Optional[str]=Field(default=None, max_length=100)

class EstoqueUpdate(BaseModel):
    quantidade_minima: Optional[int] = Field(
        default=None,
        ge=0
    )

    localizacao: Optional[str] = Field(
        default=None,
        max_length=100
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

        return values

class EstoqueQuantidadeUpdate(BaseModel):
    quantidade_atual: int = Field(..., ge=0)

class EstoqueResponse(BaseModel):
    id: int
    produto_id: int
    quantidade_atual: int
    quantidade_minima: int
    localizacao: Optional[str]
    estoque_baixo: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes=True)