'''s=str(input('[SEXO (M / F) ]')).strip().upper()[0]
while s not in 'MF':
    s=str(input(('DIGITE NOVAMENTE [M / F]: '))).strip().upper()[0]
print(('Sexo {} registrado com sucesso').format(s))'''

'''import random
print('TE DESAFIO A ACERTAR O NUMERO EM QUE ESTOU PENSANDO XD')
num=int(input('DIGITE UM NUMERO DE 1 A 10'))
pc= random.randint(1,10)
c=1
while pc!=num:
    num=int(input('erouuu! TENTE NOVAMENTE: '))
    c+=1
print('BOA! {} ERA A RESPOSTA'.format(pc))
print('tentativas: {} '.format(c))'''

'''num=int(input('digite um numero: '))
n=num-1
f=1
while num != 1:
    f=num*f
    num=num-1
print(f)
***
num=int(input('digite um numero: '))
f=1
'''
'''
num=int(input('digite um numero'))
f=1
print('{}! ='.format(num),end=' ')
for c in range(num,0,-1):
    f=f*c
    print(c,end=' → ')
print(f)'''

'''print('\033[31m-=-\033[m'*30)
pt=int(input('digite o \033[31mprimeiro termo\033[m '))
r=int(input('digite a \033[31mrazao\033[m'))
cont=10
print('\033[31m-=-\033[m'*30)
while cont > 0:
    print(pt, end=' → ')
    pt+=r
    cont-=1
    if cont == 0:
        cont=int(input('Deseja mais quantos termos?'))
        print('\033[31m-=-\033[m' * 30)'''









'''n1=1
n2=0
n=0
num=int(input('digite o numero de termos'))
while n!=num:
    print(n2, end=' → ')
    n2=n2+n1
    n1=n2-n1
    n=n+1
print('FIM')'''

'''c=s=num=0
while num != 999:
    num = int(input('digite um numero (999 para parar)'))
    if num!=999:
        c+=1
        s=num+s
print('a soma entre os {} numeros digitados é {}'.format(c,s))'''



'''c=1
ma=0
res='S'
num=int(input('digite um numero '))
m=num
me=num
while res !='N':
    res=str(input('deseja continuar[S/N]? ')).upper()
    if res =='S':
        num=int(input('digite um numero '))
        if num > ma:
            ma = num
        if num < me:
            me = num
        c+=1
        m=num+m
print(''A média entre os {} digitos é {}
O maior digito é {}
O menor digito é {}''.format(c,m/c,ma,me))
'''

'''v1=int(input('Digite um valor: '))
v2=int(input('Digite outro valor: '))
maior=0
ex=0
while ex==0:
    res=int(input(''           [OPÇÕES]
    [ 1 ]\033[35mSOMAR\033[m
    [ 2 ]\033[34mMULTIPLICAR\033[m
    [ 3 ]\033[32mMAIOR\033[m
    [ 4 ]\033[33mNOVOS NUMEROS\033[m
    [ 5 ]\033[31mSAIR DO PROGRAMA\033[m
[QUAL DAS OPÇÕES ACIMA VOCE DESEJA?]
''))
    print('-'*40)
    if res == 1:
        print('         {} + {} = \033[1;35m{}\033[m'.format(v1,v2,v1+v2))
    elif res == 2:
        print('         {} X {} = \033[1;34m{}\033[m'.format(v1,v2,v1*v2))
    elif res == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
        print('         O maior é \033[1;32m{}\033[m'.format(maior))
    elif res == 4:
        v1=int(input('Digite um numero: '))
        v2=int(input('Digite outro numero: '))
    elif res == 5:
        print('\033[1;31m[PROGRAMA ENCERRADO]')
        ex=1
    print('-' * 40)'''

















