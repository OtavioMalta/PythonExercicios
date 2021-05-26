print("\033[7m ola mundo\033[m gygu")

'''r1=float(input('reta 1 '))
r2=float(input('reta 2 '))
r3=float(input('reta 3 '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('é possivel formar um triangulo')
else:
    print('[ERRO] não é possivel formar um triangulo')
***
from datetime import date
ano=int(input('que ano quer analisar? Ultilize 0 para escolher o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano %4==0 and ano %100!=0 or ano % 400 == 0:
    print('o ano {} é BISSESTO'.format(ano))
else:
    print('o ano{} NÃO é BISSESTO'.format(ano))
***
sal=float(input('qual o seu salario? '))
if sal > 1250:
    print('voce receberá {}'.format(sal+(sal*10/100)))
else:
    print(('voce receberá {}'.format(sal+(sal*15/100))))
***
a=float(input('digite um numero '))
b=float(input('ddigite outro numero '))
c=float(input('digite outro '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o MAIOR numero é {}'.format(maior))
print('o MENOR numero é {}'.format(menor))
***
km= float(input('digite a quantidade de km rodados: '))
if km <=200:
    print('o valor a a ser cobrado é de R$ {}'.format(km*0.5))
else:
    print('o valor a ser cobrado é de {}'.format(km*0.45))
***
num=int(input('digite um numero: '))
res = num%2
if res == 0:
    print('PAR')
else:
    print('IMPAR')
***
vel=float(input("qual a velocidade do carro? "))
mul = (vel-80)*7
if vel > 80:
    print('MULTADO! Voce ultrapassou o limie de velocidade')
    print(' sua multa é de {:.2f}'.format(mul))
else:
    print('Tenha um bom dia! Dirija com segurança!')
***
import random
from time import sleep
print('_._'*20)
esc=int(input("Esolha um numero entre 0 a 5: "))
print('_._'*20)
num = random.randrange(0,5)
print('PROCESSANDO...')
sleep(2)
if num==esc:
    print('Parabens vc acertou, o numero era {}'.format(num))
else:
    print("XD numero errado, a resposta era {}".format(num))
***
'''