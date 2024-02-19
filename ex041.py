#programa que leia o ano de nascimento de um atleta e mostrando sua categoria:
from datetime import date
atual = date.today().year
nasc = int(input('Seu ano de nascimento:'))
idade = atual - nasc
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
