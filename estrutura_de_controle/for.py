
palavra = 'computador'

for letra in palavra:
    print(letra, end=" ")

print('Fim!')

aprovados = ['Rafaela', 'Vinicius', 'Paulo', 'Renata']
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça','Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in {1, 2, 3, 4}:
    print(letra)    


produto= {'Nome': 'Caneta', 'Preco':14.99, 'Importado': True,
            'estoque': 793}
for chave in produto.keys:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)



