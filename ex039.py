from datetime import date
atual = date.today().year
nasc = int(input('\033[1;36mDigite seu ano de nascimento:\033[1;36m'))
idade = atual - nasc
print(f'\033[1;33mQuem nasceu em {nasc} tem {idade} anos em {atual}\033[1;33m')
if idade == 18:
    print('\033[0;31mVocê deve se alistar imediatamente!\033[0;31m')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'\033[0;32mAinda faltam {saldo} anos para o alistamento!')
    print(f'seu alistamento será em {ano}\033[0;32m')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'\033[0;30;41mVocê deveria ter se alistado a {saldo} anos!\033[0;30;41m')
    print(f'\033[0;30;41mSeu alistamento foi em {ano}!\033[0;30;41m')
