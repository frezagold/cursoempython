while True:
    p = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if p < 0:
        break
    for c in range(1, 11):
        print(f'{p} X {c} = {p*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO!,volte sempre!')