import random

pontos = 100
nivel = 0
acertos = []
erros = []
questoes = {}

def resposta_certa(resposta):
    acertos.append(resposta)

def resposta_errada(resposta):
    erros.append(resposta)
    if nivel == 'F':
        pontos -= 20
    elif nivel == 'M':
        pontos -= 7
    elif nivel == 'D':
        pontos -= 4

def mostrar_acertos():
    print ('Acertos:', *acertos, sep = ', ')

def mostrar_erros():
    print('Erros:', *erros, sep = ', ')

