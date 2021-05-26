def metade(metade,mostrar=False):
    metade/=2
    if mostrar:
        return moeda(metade)
    else:
        return metade
def dobro(dobrar,mostrar=False):
    dobrar*=2
    if metade:
        return moeda(dobrar)
    else:
        dobrar
def aumentar(numero,acrescentar,mostrar=False):
    numero=acrescentar/100*numero+numero
    if mostrar:
        return moeda(numero)
    else:
        return numero
def diminuir(num,diminuir,mostrar=False):
    num=num-diminuir/100*num
    if mostrar:
        return moeda(num)
    else:
        return num
def moeda(valor):
    valor=f'R${valor:5.2f}'
    return valor
def resumo(preco,acr=0,dim=0):
    print('-'*30)
    print(f'Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'O Dobro  é:\t\t\t\t{dobro(preco,True)}')
    print(f'A Metade é:\t\t\t\t{metade(preco,True)}')
    print(f'{acr}% de aumento: \t\t{aumentar(preco,acr,True)}')
    print(f'{dim}% de redução: \t\t{diminuir(preco,dim,True)}')
    print('-'*30)
