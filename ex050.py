soma = 0
cont = 0
for n in range(1, 7):
    nu1 = int(input(f'\033[1;32mDigite o {n} valor: \033[1;32m'))
    if nu1 % 2 == 0:
        soma += nu1
        cont += 1
print(f'\033[0;34mVocê informou {cont} números PARES e a soma foi {soma}!\033[0;34m')

