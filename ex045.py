from random import randint
from time import sleep
print(f'{" JOGO JOKENPÔ ":=^40}')
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''\033[1;32mESCOLHA SUA JOGADA!\033[1;32m
\033[0;34m[ 0 ] pedra\033[0;34m
\033[0;35m[ 1 ] papel\033[0;35m
\033[0;36m[ 2 ] tesoura\033[0;36m''')
jogador = int(input('\033[0;37mSua escolha:\033[0;37m '))
print('\033[0;32mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('\033[0;36m-=\033[0;36m' * 15)
print(f'\033[1;31mComputador jogou {itens[computador]}\033[1;31m')
print(f'\033[1;34mjogador jogou {itens[jogador]}\033[1;34m')
print('\033[0;36m-=\033[0;36m' * 15)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
