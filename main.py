from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Processo(BaseModel):
    numero_cnj: str
    vara: str
    status: str
    valor_causa: str


lista_processos = []


@app.get("/")
def boas_vindas():
    return {'mensagem': 'API do Sistema Jurídico no ar'}


@app.get('/processos')
def exibir_processos():
    return lista_processos


@app.get('/processos/{numero_cnj}')
def consultar_processo(numero_cnj: str):
    for processo in lista_processos:
        if numero_cnj == processo.get('numero_cnj'):
            return processo

    raise HTTPException(status_code=404, detail='Processo não encontrado')


@app.post('/processos', status_code=201)
def cadastrar_processo(processo: Processo):
    for p in lista_processos:
        if processo.numero_cnj == p['numero_cnj']:
            raise HTTPException(status_code=409, detail='Processo já cadastrado')
    lista_processos.append(processo.model_dump())
    return processo


@app.put('/processos/{numero_cnj}')
def atualizar_processo(numero_cnj: str, processo: Processo):
    if processo.numero_cnj != numero_cnj:
        raise HTTPException(status_code=400, detail='Não é permitido alterar o número CNJ do processo.')
    for indice, proc in enumerate(lista_processos):
        if numero_cnj == proc['numero_cnj']:
            lista_processos[indice] = processo.model_dump()
            return processo
    raise HTTPException(status_code=404, detail='Processo não encontrado')


@app.delete('/processos/{numero_cnj}', status_code=204)
def deletar_processo(numero_cnj: str):
    for indice, processo in enumerate(lista_processos):
        if numero_cnj == processo['numero_cnj']:
            del lista_processos[indice]
            return
    raise HTTPException(status_code=404, detail='Processo não encontrado.')