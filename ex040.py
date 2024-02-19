nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
cal = (nota1 + nota2) / 2
if cal < 5.0:
    print(f'\033[0;31mA sua média ficou {cal:.1f} e você esta REPROVADO!\033[0;31m')
elif cal >= 7.0:
    print(f'\033[0;34mA sua média ficou {cal:.1f} e você esta APROVADO!\033[0;34m')
elif cal >= 5.0:
    print(f'\033[0;33mA sua média ficou {cal:.1f} e você esta de RECUPERAÇÃO!\033[0;33m')

