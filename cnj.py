import re


def normalizar_cnj(numero_cnj: str) -> str:
    """Calcula o dígito verificador do número CNJ (módulo 97, Resolução CNJ nº 65/2008)."""
    numero = numero_cnj.strip()
    if re.fullmatch(r'\d{20}', numero):
        numero = f'{numero[0:7]}-{numero[7:9]}.{numero[9:13]}.{numero[13]}.{numero[14:16]}.{numero[16:]}'
    if not re.fullmatch(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', numero):
        raise ValueError('Número CNJ em formato inválido. Exemplo: "NNNNNNN-DD.AAAA.J.TR.OOOO" ou "NNNNNNNDDAAAAJTROOOO".')
    if calcular_digito_verificador(numero) != int(numero[8:10]):
        raise ValueError('Dígito verificador do número CNJ inválido. Confira se o número foi digitado corretamente.')
    return numero


def calcular_digito_verificador(numero: str) -> int:
    digitos = numero.replace('-', '').replace('.', '')
    numero_sequencial = digitos[0:7]
    ano_ajuizamento = digitos[9:13]
    segmento_judiciario = digitos[13]
    tribunal = digitos[14:16]
    unidade_origem = digitos[16:]
    zeros_finais = '00'
    numero_montado = numero_sequencial + ano_ajuizamento + segmento_judiciario + tribunal + unidade_origem + zeros_finais
    resto = int(numero_montado) % 97
    return 98 - resto