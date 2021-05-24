import random

pontos = 100
nivel = 0
acertos = {}
erros = {}
questoes = [
    #Questão 1:
    {
        'enunciado': 'Quem são as pessoas que são grupos de risco?',
        'opcoes': [
            'a) Idosos',
            'b) Crianças',
            'c) Idosos e pessoas que sofrem com outras infecções ou doenças.',
            'd) Jovens',
            'e) Todas as pessoas são grupos de risco'
        ],
        'resposta': 2,
        'explicacao': 'Idosos estão mais propensos a desenvolver uma forma grave da COVID-19 e/ou ter complicações. Pessoas que já sofrem com outras infecções ou doenças também correm maior risco de ter seu estado de saúde seriamente agravado.',
        'pontos': 20,
        'nivel': 'F'
    },
    #Questão 2:
    {
        'enunciado': 'Quais são os principais sintomas da COVID-19?',
        'opcoes': [
            'a) Fraqueza, febre, tosse seca e, às vezes, dificuldade respiratória.',
            'b) Espirros e coriza',
            'c) Apenas dificuldade respiratória',
            'd) Todos os sintomas de gripes e/ou resfriados',
            'e) Dificuldade de concentração',
        ],
        'resposta': 0,
        'explicacao': 'Os principais sintomas incluem fraqueza, febre, tosse seca e, às vezes, dificuldade respiratória. No entanto, pacientes com a COVID-19 não costumam apresentar espirros e coriza, sintomas comuns em outras gripes ou resfriados.',
        'pontos': 7,
        'nivel': 'M'
    },
    #Questão 3:
    {
        'enunciado': 'Como e onde surgiu o coronavírus?',
        'opcoes': [
            'a) O coronavírus veio dos morcegos e foi visto pela primeira vez no Brasil.',
            'b) Acredita-se que o vírus SARS-CoV-2 tenha vindo de morcegos na China.',
            'c) O coronavírus foi fabricado em laboratório na China.',
            'd) Não se sabe onde e como o coronavírus surgiu.',
            'e) O coronavírus é uma invenção para prejudicar a economia que surgiu nos Estados Unidos.'
        ],
        'resposta': 1,
        'explicacao': 'Acredita-se que o vírus SARS-CoV-2 tenha vindo de morcegos na cidade de Wuhan, na China. Médicos chineses acreditam que o primeiro paciente seja um homem de 55 anos, que teria contraído a doença em 17 novembro do ano passado. Só conhecendo o paciente que primeiro manifestou a doença, os especialistas poderão ter mais respostas sobre a origem do vírus. O boato de que o SARS-CoV-2 tenha sido criado em laboratório não é verdadeiro: um estudo realizado por pesquisadores dos Estados Unidos, Escócia e Austrália comprova que o vírus surgiu a partir de processos naturais de evolução e que ele apresenta mutações tão aleatórias que seria improvável a manipulação humana.',
        'pontos': 4,
        'nivel': 'D'
    },
    #Questão 4:
    {
        'enunciado': 'O que é coronavírus?',
        'opcoes': [
            'a) É uma doença transmitida por um protozoário.',
            'b) É uma doença causada por um vírus.',
            'c) É uma doença que é causada apenas em animais.',
            'd) É uma doença causada por uma bactéria.',
            'e) Nenhuma das alternativas anteriores.'
        ],
        'resposta': 1,
        'explicacao': 'Segundo a Organização Mundial da Saúde (OMS), o coronavírus é uma família de vírus que pode causar doenças em animais ou humanos. Em humanos, esses vírus provocam infecções respiratórias que podem ser desde um resfriado comum até doenças mais severas como a Síndrome Respiratória do Oriente Médio (MERS) e a Síndrome Respiratória Aguda Grave (SARS). O novo coronavírus causa a doença chamada COVID-19.',
        'pontos': 20,
        'nivel': 'F'
    },
    #Questão 5:
    {
        'enunciado': 'Quanto tempo o coronavírus permanece ativo em diferentes superfícies?',
        'opcoes': [
            'a) Aproximadamente 6 dias',
            'b) Aproximadamente 5 meses',
            'c) Aproximadamente 40 minutos e até 2h30min',
            'd) Aproximadamente 1 ano',
            'e) Aproximadamente 2 meses'
        ],
        'resposta': 2,
        'explicacao': 'As partículas virais liberadas junto com a saliva podem permanecer flutuando no ar por cerca de 40 minutos e até 2h30min. Os vírus que se depositam sobre uma superfície, dependendo das características dessa superfície, podem permanecer viáveis por algumas horas ou até dias. Estudo recente, publicado no New England Journal of Medicine, descobriu que o vírus é viável por até 72 horas em plásticos e aço inoxidável, 24 horas em papelão e quatro horas em cobre. A quantidade de vírus existentes nas superfícies vai diminuindo com o passar das horas, reduzindo o risco de contaminação. O mais importante é evitar tocar em superfícies com as quais muitas pessoas têm contato, o que inclui mesas, bancadas, maçanetas, interruptores, telefones, teclados, torneiras etc. A limpeza das superfícies com desinfetante ou sabão é muito eficaz.',
        'pontos': 7,
        'nivel': 'M'
    },
    #Questão 6:
    {
        'enunciado': 'Antibióticos são eficazes na prevenção ou tratamento de Covid-19?',
        'opcoes': [
            'a) Não. São eficazes apenas para prevenção de Covid-19.',
            'b) Sim. São eficazes tanto na prevenção quanto no tratamento.',
            'c) Não. São eficazes apenas para o tratamento de Covid-19.',
            'd) Não. Não são eficazes na prevenção nem no tratamento.',
            'e) Sim. Antibióticos podem ser usados para todas as doenças.'
        ],
        'resposta': 3,
        'explicacao': 'Não. Os antibióticos não funcionam contra vírus, eles funcionam apenas em infecções bacterianas. A Covid-19 é causada por um vírus, portanto os antibióticos não funcionam. Antibióticos não devem ser usados ​​como um meio de prevenção ou tratamento de Covid-19. Eles devem ser usados ​​conforme indicação médica para tratar uma infecção bacteriana.',
        'pontos': 4,
        'nivel': 'D'
    },
    #Questão 7:
    {
        'enunciado': 'Qual a diferença entre gripe e coronavírus?',
        'opcoes': [
            'a) Os principais sintomas que diferem as duas doenças são a dor de cabeça presente na gripe e a pressão baixa e dor de garganta presente no coronavírus.',
            'b) Não existe diferença entre gripe e coronavírus.',
            'c) A diferença é que o coronavírus não apresenta febre frequente.',
            'd) Todos os sintomas são diferentes.',
            'e) A diferença é que a gripe não apresenta tosse frequente.'
        ],
        'resposta': 0,
        'explicacao': 'Os principais sintomas de Gripe são febre, tosse, calafrio, dor no corpo e mal estar, falta de ar e dor de cabeça. E os principais sintomas do coronavírus são febre, tosse, calafrio, dor no corpo e mal estar, falta de ar, pressão baixa e dor de garganta.',
        'pontos': 7,
        'nivel': 'M'
    },
    #Questão 8:
    {
        'enunciado': 'O coronavírus pode deixar sequelas?',
        'opcoes': [
            'a) Sim. Todas as pessoas que testaram positivo tiveram sequelas.',
            'b) Não. Nenhuma pessoa teve sequelas.',
            'c) Sim. Mas são apenas a minoria das pessoas.',
            'd) Sim. A maioria das pessoas que testaram positivo tiveram sequelas.',
            'e) Nenhuma das alternativas.'
        ],
        'resposta': 2,
        'explicacao': 'Na maioria dos casos, não deixa. Mas, em casos graves pode resultar em danos na função respiratória, danos neurológicos, cardiológicos, etc.',
        'pontos': 7,
        'nivel': 'M'
    },
    #Questão 9:
    {
        'enunciado': 'Qual foi o primeiro país a começar a vacinação contra o coronavírus?',
        'opcoes': [
            'a) Brasil',
            'b) Reino Unido',
            'c) China',
            'd) Estados Unidos',
            'e) Austrália'
        ],
        'resposta': 1,
        'explicacao': 'O Reino Unido foi o primeiro país que iniciou, de forma oficial, a vacinação de sua população contra a doença. Margaret Keenan, uma senhora de 90 anos, tornou-se a primeira pessoa a receber a imunização. Uma operação de guerra foi montada a fim de garantir que a vacina da farmacêutica norte-americana Pfizer, desenvolvida em parceria com a empresa de biotecnologia alemã BioNTech, chegue em segurança aos hospitais que aplicarão as doses.',
        'pontos': 4,
        'nivel': 'D'
    },
    #Questão 10:
    {
        'enunciado': 'Existe uma vacina disponível para o coronavírus?',
        'opcoes': [
            'a) Não, a vacina ainda está em desenvolvimento.',
            'b) Sim, pois a vacina da gripe também é eficaz para o coronavírus.',
            'c) Não, nem se ouve falar sobre a vacina.',
            'd) Sim, já existe vacina, porém só em alguns países.',
            'e) Sim, já existe vacina para o coronavírus no mundo todo.'
        ],
        'resposta': 4,
        'Explicação': 'Já existe uma vacina para o coronavírus. Em maio de 2021, algumas vacinas contra a COVID-19 receberam autorização para uso em países específicos, porém atualmente já existe em todos os países. Infelizmente, ainda não são todas as pessoas que têm acesso a elas. Outros imunizantes continuam sendo avaliados.',
        'pontos': 20,
        'nivel': 'F'
    }
]
opcoes_possiveis = ['A','B','C','D','E']
questao_atual = 0

def configura_jogo():
    random.shuffle(questoes)

def mostra_questao():
    questao = questoes[questao_atual]
    enunciado = questao.get('enunciado')
    opcoes = questao.get('opcoes')
    numero_questao = questao_atual + 1
    print(f'{numero_questao}. ', enunciado)
    for opcao in opcoes:
        print(opcao)

def escolhe_opcao():
    opcao_escolhida = input('Resposta: ').upper()
    while opcao_escolhida not in opcoes_possiveis:
        opcao_escolhida = input('Resposta inválida. Responda novamente: ').upper()
    return opcao_escolhida

def converte_opcao(opcao_escolhida):
    resposta = opcoes_possiveis.index(opcao_escolhida)
    return resposta

def atualiza_jogo():
    global questao_atual
    questao_atual += 1
    print('\n')

# Dados da questão
# questao = questoes[questao_atual]
# questao.get('resposta')
# questao.get('explicacao')
# questao.get('pontos')
# questao.get('nivel')

def resposta_certa(questao_atual, opcao_escolhida):
    acertos[questao_atual+1] = opcao_escolhida

def resposta_errada(questao_atual, opcao_escolhida):
    global pontos
    erros[questao_atual+1] = opcao_escolhida
    questao = questoes[questao_atual]
    if questao.get('nivel') == 'F':
        pontos -= 20
    elif questao.get('nivel') == 'M':
        pontos -= 7
    elif questao.get('nivel') == 'D':
        pontos -= 4

def mostrar_acertos():
    print ('\nAcertos:')
    for par in acertos.items():
        print(par)

def mostrar_erros():
    print('\nErros:')
    for par in erros.items():
        print(par)

def main():
    configura_jogo()
    while questao_atual <= 9:
        mostra_questao()
        opcao_escolhida = escolhe_opcao()
        resposta = converte_opcao(opcao_escolhida)
        questao = questoes[questao_atual]
        if resposta != questao.get('resposta'):
            resposta_errada(questao_atual, opcao_escolhida)
            print('\nSua resposta está errada. Explicação:', questao.get('explicacao'))
        else:
            resposta_certa(questao_atual, opcao_escolhida)
            print('\nParabéns. Sua resposta está correta.')
        atualiza_jogo()
    print('')
    mostrar_acertos()
    mostrar_erros()
    print('\nPontuação Total:', pontos)
    
main()
