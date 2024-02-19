num = int(input('Digite um número inteiro:'))
print('''\033[1;35mEscolha uma das bases para conversão:\033[1;35m
\033[0;34m[1] Binário
[2] Octal
[3] Hexadecimal\033[0;34m''')
escolha = int(input('\033[0;33mSua opção: \033[0;33m'))
if escolha == 1:
    print(f'\033[0;32m{num} convertido para binário é igual a {bin(num)[2:]}\033[0;32m')
elif escolha == 2:
    print(f'\033[0;32m{num} convertido para octal é igual a {oct(num)[2:]}\033[0;32m')
elif escolha == 3:
    print(f'\033[0;32m{num} convertido para hexadecimal é igual a {hex(num)[2:]}\033[0;32m')
else:
    print('\033[0;31mOpção inválida!\033[0;31m')
