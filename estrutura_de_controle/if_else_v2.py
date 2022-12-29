
def faixa_etaria(idade):
    if 0 <= 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade invalida'


if __name__ == '__main__':
    for idade in (17, 35, 78, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
