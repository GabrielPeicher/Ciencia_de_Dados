import pandas as pd

# Carregar o dataset
df = pd.read_csv('vendas_de_ingressos.csv')

# Exibir a quantidade de linhas e colunas do data frame
print("Quantidade de linhas e colunas:", df.shape)

# Exibir as 7 primeiras linhas do data frame
print("As 7 primeiras linhas:")
print(df.head(7))

# Exibir as 10 últimas linhas do data frame
print("As 10 últimas linhas:")
print(df.tail(10))

# Renomear as colunas de forma permanente
df.rename(columns={
    'Age': 'Idade',
    'Ticket_Price': 'Preco_do_Ingresso',
    'Movie_Genre': 'Genero',
    'Seat_Type': 'Tipo_de_Assento',
    'Number_of_Person': 'Numero_de_Pessoas',
    'Purchase_Again': 'Compraria_Novamente'
}, inplace=True)

# Resumo estatístico dos dados numéricos
print("Resumo estatístico dos dados numéricos:")
print(df.describe())

# Filtrar os dados por gênero
generos = df['Genero'].unique()
print("Gêneros de filmes:")
print(generos)

# Exibir os dados das linhas 12 a 20 (inclusive)
print("Dados das linhas 12 a 20 (inclusive):")
print(df.iloc[11:20])

# Exibir os dados das linhas 35, 38, 42 e 50
print("Dados das linhas 35, 38, 42 e 50:")
print(df.iloc[[34, 37, 41, 49]])

# Exibir os dados em que o tipo de assento é Standard
print("Dados em que o tipo de assento é Standard:")
print(df[df['Tipo_de_Assento'] == 'Standard'])

# Exibir os dados em que as idades dos consumidores está entre 20 (inclusive) e 45 anos (inclusive)
print("Dados em que as idades dos consumidores estão entre 20 e 45 anos (inclusive):")
print(df[(df['Idade'] >= 20) & (df['Idade'] <= 45)])

# Criar um novo data frame em que o gênero dos filmes assistidos é Comedy
df_comedy = df[df['Genero'] == 'Comedy']
print("Novo data frame com filmes do gênero Comedy:")
print(df_comedy)

# Criar um novo data frame exibindo os registros de Preço do Ingresso, Gênero e Tipo de Assento nos clientes que comprariam novamente
df_compraria_novamente = df[df['Compraria_Novamente'] == 'Yes'][['Preco_do_Ingresso', 'Genero', 'Tipo_de_Assento']]
print("Novo data frame com clientes que comprariam novamente:")
print(df_compraria_novamente)

# Criar uma nova series filtrando os dados pelo Tipo de Assento
series_tipo_assento = df['Tipo_de_Assento']
print("Series filtrada pelo Tipo de Assento:")
print(series_tipo_assento)

# Excluir a coluna Ticket_ID de forma permanente
df.drop(columns=['Ticket_ID'], inplace=True)

# Verificar a quantidade de valores nulos no dataset
print("Quantidade de valores nulos no dataset:")
print(df.isnull().sum())

# Verificar a quantidade de valores NaN no dataset
print("Quantidade de valores NaN no dataset:")
print(df.isna().sum())

# Utilizar o método iloc para exibir as linhas 15 a 20, e as colunas Idade, Preco_do_Ingresso e Genero
print("Linhas 15 a 20, colunas Idade, Preco_do_Ingresso e Genero:")
print(df.iloc[14:20][['Idade', 'Preco_do_Ingresso', 'Genero']])

# Utilizar o método iloc para exibir as linhas 3, 8, 10 e 13, e as colunas Genero e Numero_de_Pessoas
print("Linhas 3, 8, 10 e 13, colunas Genero e Numero_de_Pessoas:")
print(df.iloc[[2, 7, 9, 12]][['Genero', 'Numero_de_Pessoas']])