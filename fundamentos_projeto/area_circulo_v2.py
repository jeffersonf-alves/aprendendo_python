#!/usr/local/bin/python3
from math import pi


print('Nome do módulo', __name__)

if __name__ == '__main__':
    raio = input("Informe o raio: ")
    print('Area do circulo', pi* float(raio) ** 2)



