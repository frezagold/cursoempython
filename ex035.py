print('\033[0;37m=-\033[0;37m' * 30)
print('\033[1;35mANALISADOR DE TRIANGULO\033[1;35m')
print('\033[0;37m-=\033[0;37m' * 30)
a = float(input('\033[0;33mprimeiro segmento:\033[0;33m'))
b = float(input('\033[0;33msegundo segmento:\033[0;33m'))
c = float(input('\033[0;33mterceiro segmwnto:\033[0;33m'))
if a < b + c and b < a + c and c < a + b:
    print('\033[0;32mO segmento acima podem formar um triângulo!\033[0;32m')
else:
    print('\033[0;31mO segmento acima não podem formar um triângulo!\033[0;31m')

