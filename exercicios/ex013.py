from random import randint
from time import sleep
from operator import itemgetter
from datetime import date
#ex 90

'''aluno={}
aluno['nome']=str(input('NOME DO(A) ALUNO(A) '))
aluno['media']=float(input(f'MÉDIA DO(A) {aluno["nome"]} '))
if aluno['media'] >= 7:
    aluno['situação']='APROVADO!'
elif 5<=aluno['media'] < 7:
    aluno['situação']='RECUPERAÇÃO!'
else:
    aluno['situação']='REPROVADO!'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
'''

#ex 91

'''ranking=[]
jogo={'jogador 1':randint(1,6),
      'jogador 2':randint(1,6),
      'jogador 3':randint(1,6),
      'jogador 4':randint(1,6),
      }
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('---RESULTADO---')
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c,i in enumerate(ranking):
    print(f'{c+1}° Lugar : {i[0]} com {i[1]}')
    sleep(1)'''


#ex 92

'''pessoa={}
pessoa['nome']=str(input('Digite seu nome: '))
ano=int(input(('Ano de nascimento: ')))
pessoa['idade']=date.today().year-ano
pessoa['carteira de trabalho']=int(input('Carteira de trabalho(0 não tem): '))
if pessoa['carteira de trabalho']!=0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria']= pessoa['ano de contratação'] + 35 - date.today().year + pessoa['idade']
    print('-='*30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
    sleep(1)'''

#ex 93

'''tot=c=0
gols=[]
jgd={}
jgd['nome']=str(input('Nome do jogador: ')).title()
prt=int(input('Total de partidas jogadas: '))
for g in range(0,prt):
    gols.append(int(input(f'Goals marcados na partida {g+1}:')))
    tot+=gols[g]
jgd['gols']=gols
jgd['total']=tot
print(jgd)
print('=*-'*30)
for k,v in jgd.items():
    print(f'{k} tem o valor {v}.')
print('=*-'*30)
print(f'O jogador {jgd["nome"]} jogou {len(jgd["gols"])} partidas.')
for t in range(0,len(jgd['gols'])):
    print(f'  => Na partida {c + 1}, fez {gols[c]}.')
    c+=1
print(f'Foi um total de {jgd["total"]} gols marcados.')'''

#ex 94

'''m=[]
geral=[]
ps={}
id=c=0
res='S'
while res == 'S':
    ps['nome']=str(input('Nome: ')).title()
    ps['sexo']=str(input('Sexo[M / F]: ')).upper().strip()[0]
    while True:
        if ps['sexo'] in 'MF':
            break
        ps['sexo']=str(input('[ERRO] Digite um o sexo[M / F]: ')).upper().strip()[0]

    if ps['sexo']=='F':
        m.append(ps['nome'])
    ps['idade']=int(input('Idade: '))
    id+=ps['idade']
    geral.append(ps.copy())
    res=str(input('Quer continuar[S / N]? ')).upper().strip()[0]
    c+=1
print(geral)
print(f'- O grupo tem {c} pessoas')
print(f'- A média das idades é {id/c}')
print(f'- As mulheres cadastradas foram: {m}')
print(f'- As pessoas acima da média são: \n')
for p in geral:
    if p['idade']> id/c:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('>>>ENCERRADO<<<')'''

#ex 95

'''time=list()
jogador={}
partidas=list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome']=str(input('Nome do jogador: ')).upper()
    tot=int(input('Numero de partidas jogadas: '))
    for c in range (0,tot):
        partidas.append(int(input(f'Gols marcados na partida {c+1}')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('Mais algum jogador: ').upper().strip()[0])
        if resp in 'SN':
            break
        print('[ERRO] Digite um valor válido (S / N): ')
    if resp =='N':
        break
print('-='*30)
print('cod ',end='')
for c in jogador.keys():
    print(f'{c:<14}', end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca=int(input('Mostrar dados de qual jogador? (999 para parar)'))
    print('-+'*40)
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'[ERRO] Não existe jogador com código {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'    -No jogo {i+1} fez {g} gols ')
    print('-'*30)
print('<<<VOLTE SEMPRE>>>')
'''