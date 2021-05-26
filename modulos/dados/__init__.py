from modulos import cores


def leiaDin(n):
    while True:
        val = str(input(n)).replace(',', '.').strip()
        valor = val.replace('.', '')
        if valor.isnumeric():
            return float(val)
        else:
            print(f'{cores.cor(1)}[ERRO]"{val}" É um valor inválido. Tente novamente.{cores.cor(0)}')


def leiaInt(n):
    while True:
        try:
            num=int(input(n))
        except(TypeError,ValueError):
            print(cores.cor(1),'[ERRO]DIGITE UM NÚMERO INTEIRO VÁLIDO',cores.cor(0))
        except(KeyboardInterrupt):
            print(cores.cor(4),'O usuário prefiriu não digitar esse número',cores.cor(0))
            return 0
        else:
            return num

def leiaFloat(n):
    while True:
        try:
            num=float(input(n).replace(',','.'))
        except(ValueError,TypeError):
            print(cores.cor(1),'[ERRO] DIGITE UM NUMERO REAL VÁLIDO',cores.cor(0))
        except(KeyboardInterrupt):
            print(cores.cor(4),'O usuário prefiriu não digitar esse número.',cores.cor(0))
            return 0
        else:
            return num