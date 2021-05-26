m=0
mv=0
vel=''
muv=0
fem=0
for p in range(1,5):
    print('=*=*=*=*= {}° PESSOA =*=*=*=*='.format(p))
    nm = str(input('[NOME] : '))
    id=int(input('[IDADE] : '))
    sx=str(input('[SEXO M / F] :')).lower()
    m=id+m
    if id>mv:
        mv=id
        if sx=='m':
            vel=nm
    if sx=='f':
        fem+=1
        if id < 20:
            muv+=1
media= m / 4
print('=*'*20)
print('A media da idade do grupo é \033[031m{}\033[m'.format(media))
print('O homem mais velho é \033[031m{}\033[m'.format(vel.title()))
print('Há no total \033[031m{}\033[m mulher(es) com menos de 20 anos, entre as \033[031m{}\033[m apresentadas'.format(muv,fem))
print('=*'*20)
'''map=0
mep=1000000
for peso in range(1,6):
    pes=float(input('peso da {}° pessoa'.format(peso)))
    if pes>map:
        map=pes
    if pes<mep:
        mep=pes
print('O maior peso foi {}'.format(map))
print('O menor peso foi {}'.format(mep))'''

'''from _datetime import date
cont=0
hj= date.today().year
maior=0
menor=0
for c in range(1,7):
    id=int(input('ano de nascimento da primeira pessoa'))
    idade=hj-id
    if idade>=18:
        maior+=1
    else:
        menor+=1
print('há no total \033[031m{}\033[m maiores de idade e \033[031m{}\033[m menores de idade'.format(maior, menor))'''


'''fr=str(input('Digite uma frase: ')).strip().upper()
pal=fr.split()
jun=''.join(pal)
inverso=''
for inv in range(len(jun)-1,-1,-1):
    inverso+=jun[inv]
print(inverso)
if inverso==jun:
    print('é um PALINDROMO')
else:
    print('não é um PALINDROMO')'''

'''num=int(input('digite um numero: '))
tot=0
for c in range(1, num+1):
    if num % c==0:
        print('\033[36m',end=(' '))
        tot+=1
    else:
        print('\033[31m',end=(' '))
    print('{}'.format(c),end=(' '))
if tot == 2:
    print('\n \033[mé PRIMO')
else:
    print('\n \033[mnão é PRIMO')'''

'''n1=int(input('digite o primeiro numero: '))
r=int(input(('digite a razao: ')))
n=n1+(10-1)*r
for c in range(n1,n,r):
    print(c, end=(' → '))
print('ACABOU')'''

'''s=0
for c in range(1,7):
    num=int(input('digite o {} valor'.format(c)))
    if num %2==0:
        s=s+num
print('c = {}'.format(s))'''

'''cont=0
soma=0
for c in range(1,501,2):
    if c%3==0:
        soma+=c
        cont+=1
print('a soma entre os {} numeros é igual a {}'.format(cont, soma))'''


'''num=int(input('digite um numero: '))
for c in range(1,11):
    print('{} X {} = {}'.format(num,c,num*c))'''

'''for c in range(1,51):
    if c %2==0:
        print(c, end=(' '))
print('FIM')'''

'''import time
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('\033[33mFELIZ 2021!!!')'''