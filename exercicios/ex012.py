import random
#84 TAREFA

'''nome=[]
lis=[]
res='S'
maior=me=0
p=[]
l=[]
while res == 'S':
    nome.append(str(input('[NOME]')))
    nome.append(int(input('[PESO]')))
    res=input('Quer continuar? ').upper().strip()[0]
    if len(lis) == 0:
        maior=me=nome[1]
    else:
        if nome[1]<me:
            me=nome[1]
        if nome[1]>maior:
            maior=nome[1]
    lis.append(nome[:])
    nome.clear()
for n in lis:
    if n[1] == maior:
        p.append(n[0])
    if n[1] == me:
        l.append(n[0])
print(f''Foram pesadas {len(lis)} pessoas
O mais pesado é {p} com o peso {maior}
O mais leve é {l} com o peso {me}'')'''
#85

'''valor=0
parimp=[[],[]]
for c in range(0,7):
    valor=(int(input('digite um numero: ')))
    if valor %2==0:
        parimp[0].append(valor)
    else:
        parimp[1].append(valor)
parimp[0].sort()
parimp[1].sort()
print(f'Os numeros pares são: {parimp[0]}')
print(f'Os numeros impares são: {parimp[1]}')
print(*parimp)'''

'''#86/87

par=mv=tc=0
mat=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        mat[l][c]=int(input(f'Digite um numero para [{l}, {c}] '))
        if mat[l][c]%2==0:
            par+=mat[l][c]
        if c == 2:
            tc+=mat[l][c]
        if l ==1:
            if c == 0:
                mv=mat[l][c]
            if mat[l][c] > mv:
                mv=mat[l][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mat[l][c]:^3}]',end='')
    print()
print('-='*30)
print(f'A soma dos numeros pares é {par}')
print(f'O maior numero da terceira coluna é {tc}')
print(f'O maior valor da segunda linha é {mv}')'''

#88
'''num=[]
jogos=int(input('quantos jogos? '))
for j in range(0,jogos):
    for n in range (0,6):
        numero=random.randint(1,60)
        if numero not in num:
            num.append(numero)
    num.sort()
    print(f'[JOGO {j+1}]: {num}')
    num.clear()'''

#89

'''lis=[]
res='S'
c=1
aluno=[]
while res == 'S':
    aluno.append(input(F'Nome do aluno {c}: ').title())
    aluno.append(int(input(f'Nota 1 do aluno {c}: ')))
    aluno.append(int(input(f'Nota 2 do aluno {c}: ')))
    lis.append(aluno[:])
    aluno.clear()
    res=str(input('Mais algum aluno? ')).upper().strip()[0]
    c+=1
for bol in range(0,len(lis)):
    print('-='*30)
    print(f'ALUNO \033[1;34m{lis[bol][0].title()}\033[m MÉDIA: \033[1;33m{(lis[bol][1]+lis[bol][2])/2}\033[m')
print('-='*30)
while True:
    a=int(input('Deseja mostrar as notas de qual aluno?[999 para \033[1;31mfechar\033[m]'))
    if a == 999:
        break
    a-=1
    print(f''Notas de \033[1;34m{lis[a][0]}\033[m:\n Nota 1: \033[1;32m{lis[a][1]}\033[m\n NOTA 2: \033[1;33m{lis[a][2]}\033[m'')
    print('-=' * 30)
'''
