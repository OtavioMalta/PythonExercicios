
#78

'''lis=[]
posma=[]
posme=[]
for cont in range(0,5):
    lis.append(int(input('digite um valor')))
    maior=max(lis)
    menor=min(lis)
for conta in range(0,5):
    if lis[conta]==max(lis):
            posma.append(conta+1)
    elif lis[conta]==min(lis):
            posme.append(conta+1)
print(f'O maior valor é {maior} na posição',*posma, sep=' : ')
print(f'O menor valor é {menor} na posição',*posme, sep=' : ')
'''
#79

'''lista=[]
res='S'
while res =='S':
    lis=int(input('Digite um numero'))
    if lis not in lista:
        lista.append(lis)
        print('VALOR ADICIONADO COM \033[1;34mSUCESSO!\033[m')
    else:
        print('\033[1;31m[ERRO]\033[m VALOR DUPLICADO, O NUMERO NAO FOI ADICIONADO.')
    res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
lista.sort()
print(*lista, sep='...')
'''
#80(TAREFA)

'''lista=[]
for c in range(0,5):
    lis=int(input('Digite um numero '))
    if c == 0:
        lista.append(lis)
        print(f'{lista[0]} adicionado na lista')
    elif lis> max(lista):
        lista.insert(4,lis)
    elif lis<min(lista):
        lista.insert(0,lis)
    else:
        if lista[1]>lis>lista[0]:
             lista.insert(1,lis)
        elif lista[2]>lis>lista[1]:
             lista.insert(2,lis)
        elif lista[3]>lis>lista[2]:
             lista.insert(3,lis)
    print(lista)'''

#RESOLUÇÃO 80
'''lista=[]
for c in range(0,5):
    num=int(input('Digite um numero'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos=0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos+=1
    print(lista)'''

#81

'''lis=[]
res='S'
c=0
while res =='S':
    lis.append(int(input('DIGITE UM NUMERO')))
    res=str(input('Quer continuar? ')).upper().strip()[0]
print(f'Foram digitados {len(lis)} numeros')
lis.sort(reverse=True)
print(f'Ordenados de forma decrescente fica : {lis}')
if lis.count(5)>0:
    print(f'Foram digitados {lis.count(5)} numeros 5')
else:
    print('Nenhum numero 5 foi digitado')'''

#82
'''
todos=[]
par=[]
impar=[]
res='S'
while res == 'S':
    todos.append(int(input('DIGITE UM NUMERO: ')))
    res=str(input('QUER CONTINUAR?')).strip().upper()[0]
for c in todos:
    if c%2==0:
        par.append(c)
    else:
        impar.append(c)
print(f'FORAM DIGITADOS {todos}\n'
      f'PARES: {par}\n'
      f'IMPARES: {impar}')'''

#83

'''exp=[]
x=(input('DIGITE UMA EXPRESSAO MATEMATICA: ')).strip()
for c in x:
    exp.append(c)
if exp.count('(') == exp.count(')'):
    print('CORRETA')
    print(exp.count('('), exp.count(')'))
else:
    print('INCORRETA')
    print(exp.count('('), exp.count(')'))'''