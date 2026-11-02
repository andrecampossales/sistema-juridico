from fastapi import FastAPI, HTTPException

app = FastAPI()


processos = [
    {
        "numero_cnj": "1017156-44.2024.8.26.0001",
        "vara": "10ª Vara Cível",
        "status": "ATIVO",
        "valor_causa": "5000"
    },
    {
        "numero_cnj": "0007769-51.2026.8.26.0001",
        "vara": "5ª Vara Cível",
        "status": "ATIVO",
        "valor_causa": "25000"
    },
    {
        "numero_cnj": "0007066-57.2025.8.26.0001",
        "vara": "1ª Vara Cível",
        "status": "ATIVO",
        "valor_causa": "95000"
    },
]

@app.get("/")
def boas_vindas():
    return {"mensagem": "API do Sistema Jurídico no ar"}


@app.get("/processos")
def listar_processos():
    return processos


@app.get("/processos/{numero_cnj}")
def consultar_processo(numero_cnj: str):
    for processo in processos:
        if numero_cnj == processo.get("numero_cnj"):
            return processo

    raise HTTPException(status_code=404, detail='Processo não encontrado')