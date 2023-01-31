#!/usr/local/bin/python3

def fibanacci(quantidade, sequencia=(0, 11)):
    # Importante: condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibanacci(quantidade, sequencia + (sum(sequencia[-2:]), ))

if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    for fib in fibanacci(20):
        print(fib)


    
