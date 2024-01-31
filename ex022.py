nom = str(input('digite seu nome:')).strip()
print('analisando seu nome...')
print(f'seu nome em maiusculas é {nom.upper()}')
print(f'seu nome em minusculas é {nom.lower()}')
print(f'seu nomen tem {len(nom) - nom.count(' ')} letras')
separa = nom.split()
print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')

