maior = menor = p = cont = soma = 0
r = 'S'
while r not in 'N':
    p = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
    soma += p
    if cont == 1:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
