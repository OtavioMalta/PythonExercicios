nm=str(input("digite seu nome: ")).upper().strip()
nome = nm.split()
print("Muito prazer em te conhecer, {}".format(nm))
print("seu primeiro nome é {}".format(nome[0]))
print("seu ultimo nome é {}".format(nome[len(nome)-1]))

'''
let = str(input('Digite um nome: ')).upper().strip()
print('o nome {} tem {}'.format(let, let.count('A')))
print('a primeira letra A apareceu na posição {}'.format(let.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(let.rfind('A')+1))
***
name = str(input('Digite seu nome: ')).strip()
print('seu nome tem SILVA? {}'.format('silva' in name.lower()))
***
cid=str(input('Digite o nome da sua cidade: ')).strip()
print(cid[0:5].upper() == 'SANTO')
***
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num //10 % 10
c = num //100 % 10
m = num // 1000 %10
print('a unidade é {}'.format(u))
print('a dezena é {}'.format(d))
print('a centena é {}'.format(c))
print('o milhar é {}'.format(m))
***
nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, {}'.format(nome.title()))
print('seu nome em maiuscula é',nome.upper())
print('seu nome em minuscula é',nome.lower())
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
pn = nome.capitalize().split()
print('seu primeiro nome tem {}'.format(nome.find(' ')))
print('seu primeiro nome é {}'.format(pn[0]))'''
''''''












'''nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, {}'.format(nome.title()))
print('seu nome em maiuscula é',nome.upper())
print('seu nome em minuscula é',nome.lower())
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
pn = nome.capitalize().split()
print('seu primeiro nome tem {}'.format(nome.find(' ')))
print('seu primeiro nome é {}'.format(pn[0]))'''


