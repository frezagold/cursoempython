cont = soma = 0
while True:
    p = int(input('Digite um valor (999 para parar):'))
    if p == 999:
        break
    cont += 1
    soma += p
print(f'A soma dos {cont} valores foi {soma}!')
