from time import sleep
print('-=' * 30)
p1 = int(input('Primero valor:'))
p2 = int(input('Segundo valor:'))
print('-=' * 30)
s = 0
while s != 5:
    s = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>> Qual é a sua opção?'))
    if s == 1:
        print(f'A soma entre {p1} + {p2} é {p1+p2}')
    elif s == 2:
        print(f'O resultado de {p1} X {p2} é {p1*p2}')
    elif s == 3:
        if p1 > p2:
            print(f'Entre {p1} e {p2} o maior é {p1}')
        elif p2 > p1:
            print(f'Entre {p1} e {p2} o maior é {p2}')
    elif s == 4:
        print('-=' * 30)
        print('Informe os números novamente:')
        p1 = int(input('Primero valor:'))
        p2 = int(input('Segundo valor:'))
    elif s == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    sleep(2)
print('Fim do programa volte sempre!')
