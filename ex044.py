print(f'{" Lojas Do Igor ":=^40}')
preco = float(input('Digite o valor das compras:R$'))
print('''Formas de pagamento:
[1]à vista no dinheiro/cheque
[2]à vista cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
opcao = int(input('sua opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} reais, SEM JUROS!.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS!')
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE!')
print(f'Sua compra de R${preco:.2f} reais vai custar R${total:.2f} no final')
