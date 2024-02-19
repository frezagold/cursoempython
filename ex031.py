distancia = float(input('Qual a distância da sua viagem:'))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'\033[0;36mE o preço da sua dinstância será de R${preco:.2f} reais\033[0;36m')
