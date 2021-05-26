import math
import random
import 

num = float(input("digite um numero"))
print('o valor inteiro de {} é {}'.format(num, math.trunc(num)))

op=float(input('digite o cateto oposto'))
ad=float(input('digite o cateto adjacente'))
hip = math.hypot(op, ad)
print('a hipotenus vale {}'.format(hip))

ang=float(input('digite o angulo'))
sen= math.sin(math.radians(ang))
cos=math.cos((math.radians(ang)))
tan=math.tan(math.radians(ang))
print('o seno de {} é de {:.2f}'.format(ang, sen))
print('o cosseno de {} é de{:.2f}'.format(ang, cos))
print('a tangente de {} é de {:.2f}'.format(ang, tan))

n1 = input("primeiro aluno")
n2 = input('segundo aluno')
n3 = input('terceiro aluno')
n4 = input('quarto aluno')
lista =[n1,n2,n3,n4]
escolhido = random.choice(lista)
print('o escolhido foi',escolhido)

a1 = input('primeiro aluno')
a2 =input("segundo aluno")
a3 =input('terceiro aluno')
a4 = input('quarto aluno')
seq = [a1,a2,a3,a4]
random.shuffle(seq)
print('a ordem será {}'.format(seq))


