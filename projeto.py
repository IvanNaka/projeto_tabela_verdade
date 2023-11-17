import re

import ttg


def gerar_tabela(variaveis, formula):
    #Gera a tabela a partir do  truth-table-generator
    return ttg.Truths(variaveis, [formula], ints=False).as_prettytable()

def encontrar_variaveis(formula):
    regex = r'\b[a-zA-Z]\b'
    #Utiliza regex para identificar as variáveis
    variaveis_encontradas = re.findall(regex, formula)
    return set(variaveis_encontradas)

def encontrar_operacoes(formula):
    regex = r'\b(and|or|not|nor|xor|nand|implies)\b'
    operacoes_encontradas = re.findall(regex, formula)
    # Utiliza regex para identificar as operacoes
    ls_strings_operacoes = []
    dict_operacoes = {}
    # Constrói um dicionário para contagem de operações
    for operacao in operacoes_encontradas:
        if dict_operacoes.get(operacao):
            dict_operacoes[operacao] = dict_operacoes.get(operacao) + 1
        else:
            dict_operacoes[operacao] = 1
    # Cria strings formatadas para serem apresentadas ao usuário
    for op in dict_operacoes:
        if dict_operacoes[op] == 1:
            v = 'vez'
        else:
            v = 'vezes'
        ls_strings_operacoes.append(f'{op}: {dict_operacoes[op]} {v}')
    return ls_strings_operacoes


while True:
    #Recebe fórmula
    formula = input("Por favor digite a fórmula:")
    #Deixa tudo minúsculo
    formula = formula.lower()
    print(f'Fórmula em minúsculo: {formula}')
    #Encontra as variáveis
    variaveis = encontrar_variaveis(formula)
    print(f'Variáveis: {variaveis}')
    #Cria as strings com operações
    operacoes = encontrar_operacoes(formula)
    print(f'Operações:')
    for operacao in operacoes:
        print(operacao)
    #Gera a tabela
    tabela = gerar_tabela(list(variaveis), formula)
    print(tabela)
    #Recebe se o usuário quer continuar
    continuar = input('Você deseja continuar? Caso queira encerrar digite N')
    #Caso ele digite N encerra
    if continuar.lower() == 'n':
        break
