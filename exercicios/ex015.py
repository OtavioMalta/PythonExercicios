from time import sleep

# ex 101

'''from datetime import date
def voto (ano):
    idade= date.today().year-ano
    if 65>idade >=18:
        return f'{idade} anos → VOTO OBRIGATÓRIO!'
    elif 18>idade >=16 or idade >=65:
        return f'{idade} anos → VOTO OPCIONAL!'
    elif idade<16 :
        return f'{idade} anos → VOTO NEGADO'


print(voto(int(input('ANO DE NASCIMENTO: '))))'''


# ex 102

'''def fatorial(num, show):
    """show= mostrar o processo da conta
    n= o ultimo digito, no caso, o numero digitado"""
    res = 1
    n = num
    if show in 'SN':
        for c in range(0, num):
                if show == 'S':
                    print(f'{n} X', end=' ')
                    sleep(0.3)
                res *= n
                n -= 1
        print(f'= {res}')
    else:
        print( 'DADOS INVALIDOS')


fatorial(int(input('Deseja calculadr o fatorial de qual numero? ')),
         str(input('Deseja mostrar o processo da conta[S / N]? ').strip().upper()[0]))'''


#ex 103

'''def ficha(nome='', gols=''):
    if nome == '':
        nome='<DESCONHECIDO>'
    if gols.isalpha() or gols=='':
        gols=0
    print(f'O jogador {nome} fez um total de {gols} gols')


ficha(str(input('Nome do jogador: ').upper()),str(input('Gols marcados: ')))'''

#ex104

'''def leiaInt(res):
    ok=False
    valor=0
    while True:
        n = str(input(res))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print(f'\033[1;31m [ERRO] Digite um numero valido\033[m')
        if ok:
            break
    return valor'''

'''n=leiaInt('Digite um \033[33mnumero\033[m: ')
print(f'Você digitou o número \033[34m{n}\033[m')
print(type(n))'''

#ex 105

'''def notas(*num,sit=False):
    """função para analisar notas e situação de varios alunos
    param num = notas dos alunos
    sit = se deseja ou nao mostrar a situação do aluno"""
    resp={}
    media=sum(num)/len(num)
    resp['total']=len(num)
    resp['maior']=max(num)
    resp['menor']=min(num)
    resp['media']=media
    if sit:
        if media>7:
            resp['situação']='BOA'
        elif 6<media<7:
            resp['situação']='RAZOÁVEL'
        else:
            resp['situação']='RUÍM'

    return resp


resp=notas(6,5.3,9.3,10,sit=False)
print(resp)
help(notas)'''

#ex 106

'''c = ('\033[m',     # 0 - sem cor
   '\033[1;41m',   # 1 - vermelho
   '\033[1;45m',   # 2 - roxo
    '\033[7m',     # 3 - negativo
     '\033[44m',   # 4 - azul
     '\033[47m'    # 5 - cinza
)

def ajuda(aj):
    titulo(f'MOSTRANDO O MANUAL DE {aj}', 4)
    print(c[5],end='')
    help(aj)
    print(c[0],end='')
def titulo(msg,cor=0):
    print(c[cor], end='')
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))
    print(c[0],end='')


comando=''
while True:
    titulo('>>>SISTEMA DE AJUDA PYHELP<<<', 2)
    comando=str(input('FUNÇÃO OU BIBLIOTECA: ').lower())
    if comando == 'fim':
        sleep(1)
        titulo('ATÉ LOGO!',1)
        break
    else:
        ajuda(comando)
    sleep(2)'''






