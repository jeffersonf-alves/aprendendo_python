

def nota_conceito(valor):
    nota = float(valor)

    if(nota > 10):
        return 'Nota invalida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    else:
        return 'Invalido'

if __name__ == '__main__':
    nota = input('Difite a nota: ')
    conceito = nota_conceito(nota)
    print(conceito)

