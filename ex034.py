salario = float(input('qual é o salário do funcionario? R$'))
if salario <= 1250:
    print(f'\033[0;32mquem ganhava {salario} passará a ganhar { salario + (salario * 15 / 100):.2f}\033[0;32m')
else:
    print(f'\033[0;32mquem ganhava {salario} passará a ganhar { salario + (salario * 10 / 100):.2f}\033[0;32m')
