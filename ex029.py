velo = int(input('digite a sua velocidade:'))
if velo > 80:
    print(f'\033[0;31mvocê foi mutado! em um valor de {(velo-80)*7}\033[0;31m')
else:
    print('\033[0;32mvocê está na velocidade permitida, tenha um bom dia!\033[0;32m')
