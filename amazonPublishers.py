import pandas


df = pandas.read_csv('~/Downloads/bestsellers_with_categories.csv')

autores = []
autores = {x for x in df['Author'] if x not in autores}

print(len(autores))

# Há 248 autores diferentes no arquivo.

print(max(df['Price']))

# O maior preço é de 105 dólares.
