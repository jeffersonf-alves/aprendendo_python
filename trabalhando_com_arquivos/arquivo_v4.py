#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O Arquivo já foi fechado!')