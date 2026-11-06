import re


def normalizar_cnj(numero_cnj: str) -> str:
    numero = numero_cnj.strip()
    if re.fullmatch(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', numero):
        return numero
    if re.fullmatch(r'\d{20}', numero):
        return f'{numero[0:7]}-{numero[7:9]}.{numero[9:13]}.{numero[13:14]}.{numero[14:16]}.{numero[16:]}'
    raise ValueError('Número CNJ em formato inválido. Exemplo: "NNNNNNN-DD.AAAA.J.TR.OOOO" ou "NNNNNNNDDAAAAJTROOOO".')