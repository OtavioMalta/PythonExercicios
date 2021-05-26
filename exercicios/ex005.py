'''preco=float(input('qual o preço do produto? '))
pag=str(input('qual a forma de pagamento? ')).lower()
par=int(input('quantas parcelas? '))
if pag =='dinheiro' or pag == 'cheque' and par==1:
    print('[10% DE DESCONTO] O valor total é de: R$ {}'.format(preco-(preco*10/100)))
elif pag=='cartao' and par==1:
    print('[5% DE DESCONTO] O valor total é de: R$ {}'.format(preco-(preco*5/100)))
elif pag=='cartao' and par==2:
    print('[SEM JUROS] O valor total é de: R$ {}'.format(preco))
elif pag=='cartao' and par>=3:
    print('[JUROS] O valor total é de: R$ {}'.format(preco+(preco*20/100)))'''


'''peso=float(input('Qual o seu peso? '))
alt=float(input('Qual a sua altura? '))
imc=peso/alt**2
print('imc = {}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc >=18.5 and imc <25:
    print('peso ideal')
elif imc >=25 and imc <30:
    print('sobrepeso')
elif imc >=30 and imc<40:
    print('obesidade')
else:
    print('obesidade morbida')'''




'''l1=float(input('LADO 1: '))
l2=float(input('LADO 2: '))
l3=float(input('LADO 3: '))
if l1+l2>l3 and l1+l3>l2 and l3+l2>l1:
    if l1 == l2 == l3:
        tri = '\033[33mEquilátero'
    elif l1 != l2 != l3 != l1:
        tri = '\033[31mEscaleno'
    else:
        tri ='\033[35mIsóceles'
    print('É possível formar um triangulo {}'.format(tri))
else:
    print('não é possível formar um triangulo')'''

'''idad=int(input('Qual a sua idade? '))
if idad <= 9:
    print('Você se encaixa na categoria\033[32m MIRIM')
elif idad <=14 and idad> 9:
    print('Você se encaixa na categoria\033[33m INFANTIL')
elif idad <= 19 and idad > 14:
    print('Você se encaixa na categoria\033[31m JUNIOR')
elif idad == 20:
    print('Você se encaixa na categoria\033[34m SÊNIOR')
else:
    print('Você se encaixa na categoria\033[35m MASTER')'''



'''nota1=float(input('Qual a sua primeira nota? '))
nota2=float(input('Qual a sua segunda nota? '))
media=(nota1+nota2)/2
if media <5:
    print('\033[31m[REPROVADO]\033[31m')
elif media >5 and media < 6.9:
    print('\033[33m[RECUPERAÇÃO!]\033[33m')
else:
    print('\033[32m[APROVADO!]\033[32m')'''



'''id = int(input('Qual a sua idade? '))
if id > 18:
    print('Ja passou do tempo de alistamento, no total: {} anos'.format(id - 18))
elif id<18:
    print('Falta(m) {} ano(s) para o seu alistamento'.format(18- id))
else:
    print('\033[31mATENÇÃO\033[31m Voce deve se alistar esse ano!')'''

'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero:'))
if n1>n2:
    print('O primeiro valor é maior')
elif n2>n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')'''
'''valor=float(input('Qual o valor da casa? '))
sal=float(input('Qual o seu salário? '))
anos=float(input('Em quantos anos você irá pagar? '))
pres = valor / (anos*12)
if pres>sal*30/100:
    print('\033[31m[ERRO]\033[31m Emprestimo negado', pres)
else:
    print('Emprestimo \033[33m [APROVADO]\033[33m em prestações no valor de R$ {:.2f}'.format(pres))'''

'''num = int(input('Digite um numero: '))
print(''escolha uma opçao de conversão
[ 1 ]BINÁRIO
[ 2 ]OCTAL
[ 3 ]HEXADECIMAL
'')
opc=int(input('Sua opçao: '))
if opc == 1:
    print('o numero {} convertido em BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opc==2:
    print('o numero {} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc==3:
    print('o numero {} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))'''