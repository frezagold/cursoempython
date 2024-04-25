#saber se o numero é primo ou nao
num = int(input('Digite um número inteiro: '))
tot = 0
for n in range(1, num +1):
    if num % n ==0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(n, end=' ')
print(f'\nO número {num} foi divisivel {tot} vezes!')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
