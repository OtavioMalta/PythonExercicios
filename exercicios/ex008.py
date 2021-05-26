from time import sleep
'''qnt=soma=0
while True:
    num=(int(input('Digite um numero (\033[31m999\033[m para \033[31mparar\033[m): ')))
    if num == 999:
        break
    soma += num
    qnt += 1
print(f'a soma entre os \033[1;35m{qnt}\033[m numeros digitados é \033[1;36m{soma}\033[m')'''

'''while True:
    c=0
    num=int(input('Digite um numero: '))
    if num < 0:
        break
    print('-'*25)
    while c !=11:
        print(f'{num} X {c} = \033[1;34m{num*c}\033[m')
        c+=1
    print('-'*25)'''

'''v=0
from random import randint
while True:
    pc = randint(0, 10)
    parimp = str(input('PAR OU IMPAR? ')).upper().strip()[0]
    if parimp == 'P':
        pcparimp = 'I'
    else:
        pcparimp = 'P'
    num=(int(input('ESCOLHA SEU NUMERO: ')))
    print('-*'*20)
    res=(num+pc)%2 #resposta final
    if res==0:
        if parimp=='P':
            print(f'\033[1;34m[PARABÉNS!!!]\033[m Era par, TOTAL : {pc+num}')
            v+=1
            print('-*' * 20)
        else:
            print(f'\033[1;31m[GAME OVER]\033[m RESPOSTA: PAR MAQUINA: {pc} JOGADOR: {num}')
            print(f'NUMERO DE VITÓRIAS CONSECUTIVAS: {v}')
            break
    else:
        if parimp=='I':
            print(f'\033[1;34m[PARABÉNS!!!]\033[m Era impar, TOTAL : {pc+num}')
            v += 1
            print('-*' * 20)
        else:
            print(f'[\033[1;31mGAME OVER]\033[m RESPOSTA: IMPAR MAQUINA: {pc} JOGADOR: {num}')
            print(f'NUMERO DE VITÓRIAS CONSECUTIVAS: {v}')
            break'''

'''m20=c18=masc=0
while True:
    id=int(input('[IDADE]'))
    sx=' '
    while sx not in 'MF':
        sx=str(input('[SEXO (M / F)]')).upper().strip()[0]
    if id > 18:
        c18+=1
    if sx == 'M':
        masc+=1
    if sx == 'F' and id <20:
        m20+=1
    res=' '
    while res not in 'SN':
        res=str(input('deseja continuar?')).upper().strip()[0]
    if res=='N':
            break
print(f''{c18} Pessoas maiores de 18 anos
{masc} Homens
{m20} Mulheres com menos de 20 anos'')
'''
'''nmb=''
mb=mm=tot=cont=0
while True:
    nome=str(input('Qual o nome do produto? ')).upper()
    preco=int(input('Qual o preço do produto? '))
    cont+=1
    tot+=preco
    if preco > 1000:
        mm+=1
    if cont == 1 or preco<mb:
        mb=preco
        nmb=nome
    res=' '
    while res not in 'SN':
        res=str(input('Mais algum produto? ')).upper().strip()[0]
    if res in 'Nn':
        break
print('[CALCULANDO...]'),sleep(1.5)
print(f''TOTAL = \033[1;31mR$ {tot :.2f}\033[m
PRODUTOS COM VALOR SUPERIOR A R$ 1000 = \033[1;35m{mm}\033[m
O PRUDUTO MAIS ABRATO É \033[1;34m{nmb}\033[m CUSTANDO \033[1;34m{mb}\033[m'')'''

'''while True:
    print('-' * 20)
    qnt=int(input('Quanto deseja sacar? '))
    if qnt == 0:
        print('\033[1;31m[SISTEMA ENCERRADO]\033[m')
        break
    n50=qnt//50
    n20=(qnt-(n50*50))//20
    n10=(qnt-(n20*20)-(n50*50))//10
    n1=(qnt-(n50*50)-(n20*20)-(n10*10))
    print('-'*20)
    print('[PROCESSANDO]'),sleep(1.5)
    if n50>0:
        print(f'\033[1;33m{n50}\033[m CÉDULAS DE \033[1;33m50')
    if n20>0:
        print(f"\033[1;35m{n20}\033[m CÉDULAS DE \033[1;35m20")
    if n10 >0:
        print(f'\033[1;36m{n10}\033[m CÉDULAS DE \033[1;36m10')
    if n1>0:
        print(f'\033[1;34m{n1}\033[m CÉDULAS DE \033[1;34m1\033[m')'''














