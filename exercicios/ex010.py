import random

#73

'''zav='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
resp='S'
while resp == 'S':
    num = int(input('Digite um numero entre zero e vinte: '))
    while num not in range(0,21):
        num=int(input('[ERRO] Digite um numero entre 0 e 20: '))
    res=zav[num]
    print(f'Voce digitou o número \033[1;35m{res}\033[m')
    resp=str(input('Voce quer continuar? ')).upper().strip()[0]
print('\033[1;31m[PROGRAMA ENCERRADO]\033[m')'''

#74

'''tab='internacional','flamengo','atletico','fluminense','sao paulo','santos','palmeiras' ,'fortaleza','gremio','ceará','atletco go','sport','corinthians','bahia','bragantino','botafogo','vasco','atletico pr','coritiba','goias'
print(f'Os top 5 times na Tabela do Brasileirão são: {tab[0:5]}')
print('-:-'*30)
print(f'Os 4 últimos fimes na Tabela do Brasileirão são: {tab[-4:]}')
print('-:-'*30)
print(f'A tabela (em ordem alfabética) dos times é: {sorted(tab)}')
print('-:-'*30)
print(f'São Paulo está na {tab.index("sao paulo")+1}')'''
'''
n = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),)
for num in n:
    print(num, end=' → ')
print(f'\nO maior valor sorteado foi \033[1;31m{max(n)}\033[m')
print((f'O menor valor sorteado foi \033[1;35m{min(n)}'))'''

#75

'''num=int(input('digite um numero')),int(input('digite um numero')),int(input('digite um numero')),int(input('digite um numero')),int(input('digite um numero'))
print(f'Há, no total, {num.count(9)} numeros 9')
if 3 not in num:
    print('nenhum 3 foi digitado')
else:
    print(f'o valor 3 esta na posiçao {num.index(3)}')
p=0
for c in num:
    if c%2==0:
        p+=1
        if p >0:
            print('O(s) numero(s) pares é/são')
            print(c, end=' ')
        else:
            print('Não há nenhum numero par!')'''

#76

'''print('-'*40)
print(f'\033[1;31m{"Listagem de Preços" :^40}\033[m')
print('-'*40)
lista=('Lapis',1.50,
       'Caderno',30,
       'Lapizeira',3.5,
       'Mochila',50,
       'Estojo',20,
       'Marca Texto',4.5,
       'Post It',1.5,
       'Agenda',10.75,
       'Borracha',1.75,
       'Grafite',1)
for c in range(0,len(lista)):
    if c%2==0:
        print(f'{lista[c] :.<30}',end='')
        print(f' R$ {lista[c + 1]:.2f}')'''

#77

'''palavras=('azul','amarelo','verde',
        'laranja','vermelho','marrom')
for p in palavras:
    print(f'\nNa palavra {p} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''