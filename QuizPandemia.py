pontos = 100
gabarito = ['c', 'a', 'b', 'b','c','d','a','c','b','e']
resposta = []
feedback = []
def introducao():
    print('Jogo Educacional sobre a Pandemia do Coronavírus')

def pergunta1():
    print('1.Quem são as pessoas que são grupos de risco?')
    print('a)Idosos \nb)Crianças \nc)Idosos e pessoas que sofrem com outras infecções ou doenças. \nd)Jovens \ne)Todas as pessoas são grupos de risco')
    resp1 = input().lower
    resposta.append(resp1)
    
def correcao1():
    print('correção da questão 1')

def pergunta2():
    print('2.Quais são os principais sintomas da COVID-19?')
    print('a)Fraqueza, febre, tosse seca e, às vezes, dificuldade respiratória. \nb)Espirros e coriza \nc)Apenas dificuldade respiratória \nd)Todos os sintomas de gripes e/ou resfriados \ne)Dificuldade de concentração')
    resp2 = input().lower
    resposta.append(resp2)
    
def correcao2():
    print('correção da questão 2')
    
def pergunta3():
    print('3.Como e onde surgiu o coronavírus?')
    print('a)O coronavírus veio dos morcegos e foi visto pela primeira vez no Brasil. \nb)Acredita-se que o vírus SARS-CoV-2 tenha vindo de morcegos na China. \nc)O coronavírus foi fabricado em laboratório na China. \nd)Não se sabe onde e como o coronavírus surgiu. \ne)O coronavírus é uma invenção para prejudicar a economia que surgiu nos Estados Unidos.')
    resp3 = input().lower
    resposta.append(resp3)
    
def correcao3():
    print('correção da questão 3')
    
def pergunta4():
    print('4.O que é coronavírus?')
    print('a)É uma doença transmitida por um protozoário. \nb)É uma doença causada por um vírus. \nc)É uma doença que é causada apenas em animais. \nd)É uma doença causada por uma bactéria. \ne)Nenhuma das alternativas anteriores.')
    resp4 = input().lower
    resposta.append(resp4)
    
def correcao4():
    print('correção da questão 4')
    
def pergunta5():
    print('5.Quanto tempo o coronavírus permanece ativo em diferentes superfícies?')
    print('a)Aproximadamente 6 dias \nb)Aproximadamente 5 meses \nc)Aproximadamente 40 minutos e até 2h30min \nd)Aproximadamente 1 ano \ne)Aproximadamente 2 meses')
    resp5 = input().lower
    resposta.append(resp5)
    
def correcao5():
    print('correção da questão 5')
    
def pergunta6():
    print('6.Antibióticos são eficazes na prevenção ou tratamento de Covid-19?')
    print('a)Não. São eficazes apenas para prevenção de Covid-19. \nb)Sim. São eficazes tanto na prevenção quanto no tratamento. \nc)Não. São eficazes apenas para o tratamento de Covid-19. \nd)Não. Não são eficazes na prevenção nem no tratamento. \ne)Sim. Antibióticos podem ser usados para todas as doenças.')
    resp6 = input().lower
    resposta.append(resp6)
    
def correcao6():
    print('correção da questão 6')
    
def pergunta7():
    print('7.Qual a diferença entre gripe e coronavírus?')
    print('a)Os principais sintomas que diferem são a dor de cabeça presente na gripe e a pressão baixa e dor de garganta presente no coronavírus.\nb)Não existe diferença.\nc)A diferença é que o coronavírus não apresenta febre frequente.\nd)Todos os sintomas são diferentes.\ne)A diferença é que a gripe não apresenta tosse frequente.')
    resp7 = input().lower
    resposta.append(resp7)
    
def correcao7():
    print('correção da questão 7')
    
def pergunta8():
    print('8.O coronavírus pode deixar sequelas?')
    print('a)Sim. Todas as pessoas que testaram positivo tiveram sequelas. \nb)Não. Nenhuma pessoa teve sequelas. \nc)Sim. Mas são apenas a minoria das pessoas. \nd)Sim. A maioria das pessoas que testaram positivo tiveram sequelas. \ne)Nenhuma das alternativas.')
    resp8 = input().lower
    resposta.append(resp8)
    
def correcao8():
    print('correção da questão 8')
    
def pergunta9():
    print('9.Qual foi o primeiro país a começar a vacinação contra o coronavírus?')
    print('a)Brasil \nb)Reino Unido \nc)China \nd)Estados Unidos \ne)Austrália')
    resp9 = input().lower
    resposta.append(resp9)
    
def correcao9():
    print('correção da questão 9')
    
def pergunta10():
    print('9. Existe uma vacina disponível para o coronavírus?')
    print('a)Não, a vacina ainda está em desenvolvimento. \nb)Sim, pois a vacina da gripe também é eficaz para o coronavírus. \nc)Não, nem se ouve falar sobre a vacina. \nd)Sim, já existe vacina, porém só em alguns países. \ne)Sim, já existe vacina para o coronavírus no mundo todo.')
    resp10 = input().lower
    resposta.append(resp10)
    
def correcao10():
    print('correção da questão 10')

def main():
    introducao()
    pergunta1()
    correcao1()
    pergunta2()
    correcao2()
    pergunta3()
    correcao3()
    pergunta4()
    correcao4()
    pergunta5()
    correcao5()
    pergunta6()
    correcao6()
    pergunta7()
    correcao7()
    pergunta8()
    correcao8()
    pergunta9()
    correcao9()
    pergunta10()
    correcao10()

main()
