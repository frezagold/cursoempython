ano = int(input('Que ano quer analisar?:'))
if ano % 4 == 0 and ano % 100 != 0 or ano & 400 == 0:
    print(f'\033[0;33mo ano {ano} é bíssexto\033[0;33m')
else:
    print(f'\033[0;32mo ano {ano} não é bíssexto\033[0;32m')