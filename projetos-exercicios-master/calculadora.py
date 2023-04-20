while True:
    print('-='*20)
    p1 = float(input('Qual o primeiro valor? '))
    print('-='*20)
    print(f'{p1} ? ')
    print('-='*20)
    operacao = str(input('[ + ] Soma\n'
                         '[ - ] Subtração\n'
                         '[ X ] Multiplicação\n'
                         '[ / ] Divisão\n'
                         '[ V ] Raiz Quadrada\n'
                         '[ ** ] Potenciação\n'
                         'Qual a operação que você deseja fazer? ')).upper()

    print('-='*20)

    print(f'{p1} {operacao} ')

    print('-='*20)

    if operacao in ['+', '-', 'X', '/', '**']:
        p2 = float(input('Qual o segundo valor? '))

        print('-=' * 20)

        if operacao == '+':
            def somar(v1, v2):
                resultado = v1 + v2
                return resultado
            print(f'{p1} {operacao} {p2} = {somar(p1, p2)}')

        if operacao == '-':
            def subtracao(v1, v2):
                resultado = v1 - v2
                return resultado
            print(f'{p1} {operacao} {p2} = {subtracao(p1, p2)}')

        if operacao == 'X':
            def multiplicacao(v1, v2):
                resultado = v1 * v2
                return resultado
            print(f'{p1} {operacao} {p2} = {multiplicacao(p1, p2)}')

        if operacao == '/':
            def divisao(v1, v2):
                resultado = v1 / v2
                return resultado
            print(f'{p1} {operacao} {p2} = {divisao(p1, p2)}')

        if operacao == '**':
            def potenciacao(v1, v2):
                resultado = v1 ** v2
                return resultado
            print(f'{p1} {operacao} {p2} = {potenciacao(p1, p2)}')

    else:
        if operacao == 'V':
            def raiz_quadrada(v1):
                resultado = v1**0.5
                return resultado
            print(f'{operacao}{p1} = {raiz_quadrada(p1)}')

    print('-='*20)

    r = str(input('Você deseja fazer um outro calculo (Y / N)? ')).upper()
    if r == 'N':
        break
    print('-='*20)

print('-='*20)
print('Obrigado, até a próxima!')
