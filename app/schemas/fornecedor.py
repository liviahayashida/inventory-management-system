from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    model_validator
)


def validar_cnpj_valor(valor: str) -> str:
    valor = "".join(filter(str.isdigit, valor))

    if len(valor) != 14:
        raise ValueError("O CNPJ deve possuir 14 dígitos.")

    if valor == valor[0] * 14:
        raise ValueError("CNPJ inválido.")

    def calcular_digito(cnpj, pesos):
        soma = sum(
            int(digito) * peso
            for digito, peso in zip(cnpj, pesos)
        )

        resto = soma % 11

        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(
        valor[:12],
        [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    )

    segundo_digito = calcular_digito(
        valor[:12] + str(primeiro_digito),
        [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    )

    if (
        int(valor[12]) != primeiro_digito
        or int(valor[13]) != segundo_digito
    ):
        raise ValueError("CNPJ inválido.")

    return valor


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

    cnpj: str

    @field_validator("cnpj")
    @classmethod
    def validar_cnpj(cls, valor):
        return validar_cnpj_valor(valor)


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

    cnpj: str | None = None

    @field_validator("cnpj")
    @classmethod
    def validar_cnpj(cls, valor):

        if valor is None:
            return valor

        return validar_cnpj_valor(valor)

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