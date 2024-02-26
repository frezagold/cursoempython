cont = 0
print('\033[0;32m-=\033[0;32m'* 20)
print(f'{'\033[1;36m10 TERMOS DE UMA PA\033[1;36m' :>28}')
print('\033[0;32m-=\033[0;32m'* 20)
nu1 = int(input('\033[0;35mPrimeiro termo: \033[0;35m'))
nu2 = int(input('\033[0;35mRazão: \033[0;36m'))
decimo = nu1 + (10 - 1) * nu2
for n in range(nu1, decimo, nu2):
    print(f'{n}', end= ' -> ' )
print('acabou!')
