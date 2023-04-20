# Fórmula do IMC:
'''peso (kg) / altura² (metros)'''

while True:
    print('-'*30)
    m = 'Calcuradora de IMC'
    print(f'{m}')
    print('-'*30)

    peso = float(input('1) Digite o seu peso (kg): '))
    altura = float(input('2) Digite a sua altura (metros): '))
    
    def imc(peso, altura):
        imc = peso/(altura**2)
        return imc
    
    imc = imc(peso, altura)
    
    print('-'*30)
    print(f'O seu IMC é de {imc:.2f}.')


    if imc < 18.5:
        print('Você está abaixo do peso ideal!')
    elif imc <=24.9:
        print(f'Você está no peso ideal!')
    elif imc <= 29.9:
        print(f'Você está com excesso de peso!')
    elif imc <= 34.9:
        print(f'Você está com obesidade classe I.')
    elif imc <= 39.9:
        print(f'Você está com obesidade classe II.')
    elif imc >= 40:
        print(f'Você está com obesidade classe III.')
    
    print('-'*30)    
    
    cont = str(input('Calcular IMC de outra pessoa (y/n)? ')).lower()
    if cont == 'n':
        break