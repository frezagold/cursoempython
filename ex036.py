casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual seu salário: R$'))
ano = int(input('quantos anos de financiamento?'))
prestacao = casa / (ano * 12)
minimo = salario * 30 / 100
print(f'\033[1;34mPara pagar uma casa de R${casa:.2f} reais em {ano} anos a sua prestação será de R${prestacao:.2f} reais\033[1;34m')
if prestacao <= minimo:
    print('\033[0;32mSeu empréstimo foi concebido\033[0;32m')
else:
    print('\033[0;31mSeu empréstimo foi negado!\033[0;31m')