somadaidade = 0
mediaidade = 0
maioridadehomem = 0
nomedovelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----{p}º pessoa----')
    nome = str(input('Nome:')).strip()
    idade = int(input('idade:'))
    sexo = str(input('Sexo M/F:')).strip()
    somadaidade =+ idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 =+ 1
mediaidade = somadaidade / 4
print(f'A média de idade do grupo é igual a de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e o nome do mais velho é {nomedovelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
