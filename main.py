from decimal import Decimal
from enum import StrEnum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

from cnj import normalizar_cnj

app = FastAPI()


class StatusProcesso(StrEnum):
    ATIVO = 'ATIVO'
    ARQUIVADO = 'ARQUIVADO'
    EXTINTO = 'EXTINTO'
    SUSPENSO = 'SUSPENSO'


class EscritorioRepresenta(StrEnum):
    REQUERENTE = 'REQUERENTE'
    REQUERIDO = 'REQUERIDO'


class Processo(BaseModel):
    numero_cnj: str
    vara: str
    status: StatusProcesso
    valor_causa: Decimal = Field(ge=0, decimal_places=2)
    escritorio_representa: EscritorioRepresenta

    @field_validator('numero_cnj')
    @classmethod
    def validar_numero_cnj(cls, valor: str) -> str:
        return normalizar_cnj(valor)


lista_processos = []


def buscar_indice(numero_cnj: str):
    for indice, processo in enumerate(lista_processos):
        if numero_cnj == processo['numero_cnj']:
            return indice
    return None


@app.get('/')
def boas_vindas():
    return {'mensagem': 'API do Sistema Jurídico no ar.'}


@app.get('/processos', response_model=list[Processo])
def exibir_processos():
    return lista_processos


@app.get('/processos/{numero_cnj}', response_model=Processo)
def consultar_processo(numero_cnj: str):
    indice = buscar_indice(numero_cnj)
    if indice is None:
        raise HTTPException(status_code=404, detail='Processo não encontrado.')
    return lista_processos[indice]


@app.post('/processos', status_code=201, response_model=Processo)
def cadastrar_processo(processo: Processo):
    indice = buscar_indice(processo.numero_cnj)
    if indice is not None:
        raise HTTPException(status_code=409, detail='Processo já cadastrado.')
    lista_processos.append(processo.model_dump())
    return processo


@app.put('/processos/{numero_cnj}', response_model=Processo)
def atualizar_processo(numero_cnj: str, processo: Processo):
    if processo.numero_cnj != numero_cnj:
        raise HTTPException(status_code=400, detail='Não é permitido alterar o número CNJ do processo.')
    indice = buscar_indice(numero_cnj)
    if indice is None:
        raise HTTPException(status_code=404, detail='Processo não encontrado.')
    lista_processos[indice] = processo.model_dump()
    return processo


@app.delete('/processos/{numero_cnj}', status_code=204)
def deletar_processo(numero_cnj: str):
    indice = buscar_indice(numero_cnj)
    if indice is None:
        raise HTTPException(status_code=404, detail='Processo não encontrado.')
    del lista_processos[indice]
    return