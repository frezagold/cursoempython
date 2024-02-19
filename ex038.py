nu1 = int(input('Digite o primeiro número:'))
nu2 = int(input('Digite o segundo número:'))
if nu1 > nu2:
    print('\033[0;34mO primeiro valor é maior!\033[0;34m')
elif nu1 < nu2:
    print('\033[0;34mO segundo valor é maior!\033[0;34m')
else:
    print('\033[0;34mOs dois valores são iguais!\033[0;34m')