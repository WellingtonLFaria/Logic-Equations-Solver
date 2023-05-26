import random
from typing import List
from string import ascii_lowercase


def gerar_numeros(tamanho: int) -> List[int]:
    return random.sample(range(1, tamanho+1), tamanho)


def expressoes_refatoradas(expressoes: List[str]) -> List[str]:
    LETRAS = ascii_lowercase
    expressoes_novas = []
    for equacao in expressoes:
        for letra in equacao:
            if letra in LETRAS:
                equacao = equacao.replace(letra, f'x[{LETRAS.index(letra)}]')
        expressoes_novas.append(equacao)
    return expressoes_novas


def checar_expressoes(expressoes: List[str]) -> List[bool]:
    expressoes_eval = []
    for expressao in expressoes:
        expressoes_eval.append(eval(expressao))
    return expressoes_eval


def encontrar_valores_corretos(expressoes: List[str], tamanho: int) -> List[int]:
    global x
    x = gerar_numeros(tamanho)
    expressoes = expressoes_refatoradas(expressoes)
    while not all(checar_expressoes(expressoes)):
        x = gerar_numeros(tamanho)
    return x
