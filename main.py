"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Implemente as funções abaixo para calcular média, mediana e moda de uma lista de números.

Instruções:
1. Faça o fork deste repositório no seu GitHub.
2. Clone o seu fork para sua máquina.
3. Complete as funções abaixo.
4. Teste o código executando: python calculadora_estatistica.py
5. Envie um Pull Request com a sua solução.

💡 Dica: não use bibliotecas externas como numpy ou statistics.
"""

import numpy as np


# Função para calcular a média
def calcular_media(lista):
    return sum(lista) / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    if not lista:
        raise ValueError("A lista está vazia")
    sorted_list = sorted(lista)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2


# Função para calcular a moda
def calcular_moda(lista):
    if not lista:
        raise ValueError("A lista está vazia")
    counts = {}
    for v in lista:
        counts[v] = counts.get(v, 0) + 1
    max_count = max(counts.values())
    modos = [k for k, c in counts.items() if c == max_count]
    return modos[0] if len(modos) == 1 else modos


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("📊 Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
