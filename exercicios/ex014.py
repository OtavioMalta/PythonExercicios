from time import sleep
from random import randint
#ex 96

'''def area(l,c):
    a=l*c
    print(f'A area do terreno é {a} m²')


area(float(input("Largura(m):")),float(input("Comprimento(m):")))'''

#97

'''def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))


escreva(input('DIGITE SEU TEXTO AQUI:  '))'''

#ex 98
'''
def lin():
    print('-+'*20)
def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    num=inicio
    if fim>inicio:
        print(f'contagem de {inicio} até {fim} contando de {passo} em {passo}:')
        for c in range(inicio,fim+1,passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print()
    elif inicio>fim and passo>0:
        print(f'contagem de {inicio} até {fim} contando de {passo} em {passo}:')
        for c in range(inicio,fim-1,-passo):
            print(c,end=' ')
            sleep(0.5)
        print('FIM!')
        print()
    elif passo<0:
        print(f'contagem de {inicio} até {fim} contando de {-passo} em {-passo}:')
        for c in range(inicio,fim-1,passo):
            print(c,end=' ')
            sleep(0.5)
        print('FIM!')
        print()
    lin()


lin()
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem! ')
contador(int(input('Inicio: ')),int(input('Fim: ')),int(input('Passo: ')))'''

#ex 99

'''def maior(* num):
    for c in num:
        print(c,end=' ')
        sleep(0.4)
    print('Analisando os valores informados...')
    if len(num) >=1:
        print('O maior numero é:', max(num))
    else:
        print('O maior numero é 0')
    print(f'foram informados {len(num)} valores')
    print('-+'*30)


maior(5,3,7,1,0)
maior(4,7,0)
maior(1,2)
maior()'''

#ex 100

'''soma=[]
numeros=[]


def sorteia():
    print(f'Os numeros sorpteados foram:', end='')
    for c in range(0,5):
        numeros.append(int(randint(1,10)))
        print(numeros[c],end=' → ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    for c in numeros:
        if c%2==0:
            soma.append(c)
    print(sum(soma))


sorteia()
print(f'A soma dos numeros pares de {numeros} é ',end='')
somaPar()
'''
