import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, idade: {}'.format(*pessoa))

