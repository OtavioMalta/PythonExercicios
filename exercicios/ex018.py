from modulos import cores
from time import sleep
from ex115.tools import *
from ex115.arquivo import *
from modulos.dados import *


'''add=[]
nome = ['OTAVIO', 'SILVIA', 'CIDO', 'ARTHUR']
idade = [19,42,50,12]
while True:
    print('-'*30)
    print('MENU PRINCIPAL'.center(30))
    print('-'*30)
    print(f'{cores.cor(6)}1{cores.sem()} - {cores.cor(4)}VER PESSOAS CADASTRADAS{cores.sem()}')
    print(f'{cores.cor(6)}2{cores.sem()} - {cores.cor(4)}CADASTRAR NOVA PESSOA{cores.sem()}')
    print(f'{cores.cor(6)}3{cores.sem()} - {cores.cor(4)}SAIR{cores.sem()}')
    print('-'*30)
    res = int(input(f'{cores.cor(3)}SUA OPÇÃO: {cores.sem()}'))
    if res == 2:
        nome.append(str(input('NOME: ')))
        idade.append(str(input('IDADE: ')))
        add.append(nome)
        add.append(idade)
    elif res == 1:
        for c in range(0, len(nome)):
                print(f'{nome[c]:<30}',end='')
                print(f'{idade[c]:>3} anos')
    elif res == 3:
        print(cores.cor(5),cores.negr(),'>>>ENCERRANDO PROGRAMA<<<')
        break
    else:
        print(f'{cores.bg(1)}[ERRO]{cores.sem()}{cores.cor(1)} DIGITE UM VALOR VÁLIDO: {cores.sem()}')
'''
arq='cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['VER PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA','EXCLUIR UM CADASTRO','LIMPAR CADASTROS','SAIR'])
    sleep(0.7)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome=str(input('NOME: '))
        idade=leiaInt('IDADE: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        lerArquivo(arq)
        linha=str(input(f'QUAL CADASTRO DESEJA {sub()}{negr()}APAGAR{sem()}? ').title())
        delLinha(arq,linha)
    elif resposta == 4:
        delArquivo(arq)
    elif resposta == 5:
        print('>>>ENCERRANDO SISTEMA<<<')
        break
    else:
        print('[ERRO] OPÇÃO INVÁLIDA!')
