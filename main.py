from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Processo(BaseModel):
    numero_cnj: str
    vara: str
    status: str
    valor_causa: str


processos = []


@app.get("/")
def boas_vindas():
    return {'mensagem': 'API do Sistema Jurídico no ar'}


@app.get('/processos')
def listar_processos():
    return processos


@app.get('/processos/{numero_cnj}')
def consultar_processo(numero_cnj: str):
    for processo in processos:
        if numero_cnj == processo.get('numero_cnj'):
            return processo

    raise HTTPException(status_code=404, detail='Processo não encontrado')


@app.post('/processos', status_code=201)
def cadastrar_processo(processo: Processo):
    for p in processos:
        if processo.numero_cnj == p['numero_cnj']:
            raise HTTPException(status_code=409, detail='Processo já cadastrado')
    processos.append(processo.model_dump())
    return processo