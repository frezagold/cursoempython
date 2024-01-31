nome = str(input('digite uma frase:').lower().strip())
print(f'A letra A aparece {nome.count('a')}')
print(f'a primeira letra A apareceu na posição {nome.find('a')+1}')
print(f'a ultima letra A apareceu na posição {nome.rfind('a')+1}')


