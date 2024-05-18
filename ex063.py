print('-='*30)
print('Sequência de Fibonacci')
print('-='*30)
f = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print('~'*30)
print(f'{n1} -> {n2}', end='')
cont = 3
while cont <= f:
    n3 = n1 + n2
    print(f'-> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print('-> FIM', end='')
print('~'*30)
