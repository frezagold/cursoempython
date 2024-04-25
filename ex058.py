from random import randint
print('ola sou seu computador!\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    p = int(input('Qual seu palpite? '))
    palpite += 1
    if p == computador:
        acertou = True
    else:
        if p < computador:
            print('Mais... Tente mais uma vez!')
        elif p > computador:
            print('Menos... Tente mais uma vez!')
print(f'acertou com {palpite} tentativas! Parabéns')
