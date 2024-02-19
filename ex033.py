a = int(input('digite um número:'))
b = int(input('digite outro número:'))
c = int(input('digite mais um número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'\033[0;31mo menor número é o {menor}\033[0;31m')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[0;36mo maior número é o {maior}\033[0;36m')
