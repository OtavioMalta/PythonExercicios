n = int(input('digite um numero'))
s = n + 1
a = n - 1
d = n*2
t = n*3
r =n**(1/2)
print('o numero sucessor de {} é {} e o antecessor é {}'.format(n, s, a))
print('o dobro de {} é {} o triplo é {} e a raiz quadrada {}'.format(n, d, t, r))
print('a tabuada de {} é:'.format(n),n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10)

n1 = int(input('digite a primeira nota'))
n2 = int(input('digite a segunda nota'))
m = (n1 + n2)/2
print(" a media do aluno é de {}".format(m))

mts = int(input('digite um tamanho em metros'))
cm = mts * 100
mm = cm*10
print('esse numero em cm é{} e em milimetros é {}'.format(cm, mm))

rs = int(input('quantos reais vc tem?'))
dl = rs / 3.27
print('no totaal vc tem {} dolares'.format(dl))

al=int(input('altura da parede'))
lar=int(input('largura da parede'))
ar=al*lar
tin=ar/2
print('a area da parede é de {} metros quadrados, por isso precisará de {} litros de tinta'.format(ar,tin))

pr=float(input('digite um preço'))
dc= pr - (pr*5/100)
print('o preço com o desconto fica {}'.format(dc))

sal=float(input('quanto ganha o funcionario?'))
aum= sal + (sal*15/100)
print('o funcinario, com um aumento de 15%, receberá:R${}'.format(aum))

temp=float(input("qual a temperatura em Celsius"))
tmp= temp *1.8 + 32
print('a temperatura me fahrenheit é de {}'.format(tmp))

dia=int(input('quantos dias o carro foi alugado?'))
km=float(input('quantos km foram percorridos?'))
tot = (dia*60) + (0.15*km)
print('o total a ser pago é de {}'.format(tot))




