print('Gerador de PA')
print('-='*30)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} ->', end='')
    termo += razao
    c += 1
print('FIM!')
