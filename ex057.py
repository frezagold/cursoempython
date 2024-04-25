s = str(input('Informe seu sexo: [M/F]')).upper()[0]
while s not in 'FM':
    s = str(input('Dados inválidos, por favor informe seu sexo:')).upper()[0]
print(f'Sexo {s} registrado com sucesso!')
