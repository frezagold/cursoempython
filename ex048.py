soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 ==0:
        soma += n
        cont += 1
print(f'\033[0;34mA soma de todos os {cont} valores solicitados é {soma}\033[0;34m')