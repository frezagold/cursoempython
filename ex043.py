print('\033[0;36m=-\033[0;36m' * 30)
print('\033[1;34mCALCULO DE IMC!\033[1;34m')
print('\033[0;36m=-\033[0;36m' * 30)
peso = float(input('\033[0;32mdigite seu peso:Kg\033[0;32m'))
altura = float(input('\033[0;32mdigite sua altura:\033[0;32m'))
cal = peso / (altura ** 2)
if cal < 18.5:
    print('\033[0;35mABAIXO DO PESO!\033[0;35m')
elif cal < 25:
    print('\033[0;32mPESO IDEAL!\033[0;32m')
elif cal < 30:
    print('\033[0;33mSOBREPESO!\033[0;33m')
elif cal < 40:
    print('\033[0;35mOBESIDADE!\033[0;35m')
elif cal >= 40:
    print('\033[0;31mOBESIDADE MÓRBIDA\033[0;31m')
