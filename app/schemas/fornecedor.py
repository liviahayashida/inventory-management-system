from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator


class FornecedorCreate(BaseModel):

    razao_social: str = Field(
        min_length=2,
        max_length=150
    )

    email: EmailStr

    telefone: str | None = Field(
        default=None,
        max_length=20
    )

    cnpj: str = Field(
        min_length=14,
        max_length=14
    )

    @field_validator("cnpj")
    @classmethod
    def validar_cnpj(cls, valor):
        valor = "".join(filter(str.isdigit, valor))

        if len(valor) != 14:
            raise ValueError("O CNPJ deve possuir 14 dígitos.")

        return valor


class FornecedorUpdate(BaseModel):

    razao_social: str | None = Field(
        default=None,
        min_length=2,
        max_length=150
    )

    email: EmailStr | None = None

    telefone: str | None = Field(
        default=None,
        max_length=20
    )

    cnpj: str | None = Field(
        default=None,
        min_length=14,
        max_length=14
    )

    @field_validator("cnpj")
    @classmethod
    def validar_cnpj(cls, valor):
        if valor is None:
            return valor

        valor = "".join(filter(str.isdigit, valor)) #remove tudo q n é numero

        if len(valor) != 14:
            raise ValueError("O CNPJ deve possuir 14 dígitos.")

        return valor

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


class FornecedorResponse(BaseModel):

    id: int
    razao_social: str
    email: EmailStr
    telefone: str | None
    cnpj: str
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(
        from_attributes=True
    )