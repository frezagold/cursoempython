valor = int(input('Digite o número para ver sua tabuáda: '))
print('\033[0;31m=-\033[0;31m' * 10)
for n in range(0, 11):
    print(f'\033[1;35m{valor} X {n} = {valor * n}\033[1;35m')
print('\033[0;31m=-\033[0;31m' * 10)