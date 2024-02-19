from random import randint
from time import sleep
computador = randint(0, 5)
print('=-=' * 20)
print('Vou pensar em um número de 0 a 5, tente advinhar!')
print('=-=' * 20)
jogador = int(input('Digite um número de 0 a 5:'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('você acertooou!')
else:
    print(f'você errou eu pensei no número {computador}')
