from math import radians, sin, cos, tan
angulo = float(input('digite o angulo que deseja:'))
seno = sin(radians(angulo))
print(f'o angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'o angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'o angulo de {angulo} tem a tangente de {tangente:.2f}')
