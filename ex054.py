from datetime import date
atual = date.today().year
tot = 0
tot2 = 0
for n in range(1, 8):
    ano = int(input(f'\033[1;32mEm que ano a {n}° pessoa nasceu? \033[1;32m'))
    idade = atual - ano
    if idade <= 17:
        tot += 1
    else:
        tot2 += 1
print(f'\033[34mAo todo tivemos {tot} pessoas menores de idade!\033[34m')
print(f'\033[35mAo todo tivemos {tot2} pessoas maiores de idade!\033[35m')