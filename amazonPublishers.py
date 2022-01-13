import pandas


# Carrega o arquivo CSV a variável "df"
df = pandas.read_csv('~/Downloads/bestsellers_with_categories.csv')


# Cria um SET para garantir que somente valores únicos serão adicionados
autores = {}
# Set comprehension para adicionar os valores da coluna "Author" ao SET
autores = {x for x in df['Author'] if x not in autores}

# Retorna quantos autores diferentes há no arquivo
print(f'Há {len(autores)} autores diferentes no arquivo.')

# Retorno o livro com maior valor
print(f'O maior preço é de U${max(df["Price"])} e o menor é de U${min(df["Price"])}.')

# Retorna o valor médio das avalições de todos os livros
media = sum(df["User Rating"] / len(df["User Rating"]))
print(f'A avalição média desses livros é de: {media:.2f}')

# Identifica os valores que mais se repetem nas colunas "Author" e "Genre"
m_autor = df['Author'].value_counts().idxmax()
m_genero = df['Genre'].value_counts().idxmax()

print(f'O principal autor do dataset é {m_autor}')
print(f'O principal gênero literário do dataset é {m_genero}')
