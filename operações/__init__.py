def leiaInt(msg):
    n = ''
    ok = False
    while not ok:
        try:
            n = str(input(f'{msg}'))
            n = int(n)
            ok = True
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


def s():
    s = []
    while True:
        s.append(leiaInt('Digite um número: '))
        resp = ' '
        while resp not in 'SN':
            try:
                resp = str(input('Deseja somar mais um número? [S/N] ')).strip().upper()[0]
            except:
                print('\033[31mERRO! Selecione uma opção válida.\033[m')
        if resp == 'N':
            break
    f = sum(s)
    print(f'A soma entre: {s} é igual a {f}')


def sub(n1, n2):
    sub = n1 - n2
    print(f'Subtraindo {n2} de {n1} temos {sub}')


def mult(*num):
    i = []
    f = 1
    while True:
        i.append(leiaInt('Digite um número: '))
        resp = ' '
        while resp not in 'SN':
            try:
                resp = str(input('Deseja multiplicar mais um número? [S/N] ')).strip().upper()[0]
            except:
                print('\033[31mERRO! Selecione uma opção válida.\033[m')
        if resp == 'N':
            break
    for n in i:
        f *= n
    if f % 1 == 0:
        f = int(f)
    print(f'Multiplicando {i} temos como produto {f}')


def div(dividendo, divisor):
    quo = dividendo / divisor
    print(f'Dividindo {dividendo} pelo {divisor} temos resultado {quo}')
