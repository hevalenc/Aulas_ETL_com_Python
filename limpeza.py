import pandas as pd
import pandera as pa

df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)

print("\n** Mostrar as primeiras 10 linhas da tabela **")
print(df.head(10))

print("\n** Mostrar a cidade do registro na posição 1 **")
print(df.loc[1,'ocorrencia_cidade'])

print('\n** Mostrar os registros entre as posições 1 à 3 **')
print(df.loc[1:3])

print("\n** Mostrar os registros nas posições 10 e 40 **")
print(df.loc[[10,40]])

print("\n** Mostrar os registros da coluna 'ocorrencia_cidade' **")
print(df.loc[:,'ocorrencia_cidade'])

print("\n** Verificar se o tipo do dado da coluna 'codigo_ocorrencia' é único **")
print(df.codigo_ocorrencia.is_unique)

df.set_index('codigo_ocorrencia', inplace=True) #configurando uma coluna como índice

print("\n** Mostrar a tabela com a coluna 'codigo_ocorrencia' como índice **")
print(df.head())

print("\n** Mostrar o registro no novo índice '40324' **")
print(df.loc[40324])

df.reset_index(drop=True, inplace=True) #reinicializando o índice da tabela

print("\n** Mostrar a tabela com o índice reinicializado **")
print(df.head())

print("\n** Alterar a informação de um registro **")
print(df.head(1))

df.loc[0,'ocorrencia_aerodromo'] = '' #trocando o valor de um registro específico, ex.: registro 0, coluna ocorrencia_aerodromo

print(df.head(1))

print("\n** Substituindo todos os valores de uma coluna **")

df.loc[:,'total_recomendacoes'] = 10

print(df)

df['ocorrencia_uf_bkp'] = df.ocorrencia_uf #criando uma coluna clonando os registros de outra

print("\n** Mostrar a tabela com a nova coluna **")
print(df)

df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE' #alterando os valores de registros específicos

print("\n** Mostrar a tabela com a coluna 'ocorrencia_classificacao' com novos dados **")
print(df)

print("\n** Mostrar a tabela usando um filtro **")
print(df.loc[df.ocorrencia_uf == 'SP'])

print("\n** Alterando um registro **")
print(df.head())

df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA

print(df.head())

df.replace(['**','###!','####','****','*****','NULL'], pd.NA, inplace=True)

print("\n** Contar o total de dados com NA **")
print(df.isna().sum())

print("\n** Contar o total de dados com NULL **")
print(df.isnull().sum())

df.fillna(10, inplace=True) #substituir todos os valores NA por 10

print("\n** Contar o total de dados com NA **")
print(df.isna().sum())

print("\n** Contar o total de dados com NULL **")
print(df.isnull().sum())

df.replace([10], pd.NA, inplace=True)

print("\n** Contar o total de dados com NULL **")
print(df.isnull().sum())

df.fillna(value={'total_recomendacoes':10}, inplace=True)

print("\n** Contar o total de dados com NULL **")
print(df.isnull().sum())

df['total_recomendacoes_bkp'] = df.total_recomendacoes

print("\n** Mostrar a tabela com a nova coluna **")
print(df)

df.drop(['total_recomendacoes_bkp'], axis=1, inplace=True) #removendo uma coluna

print("\n** Mostrar a tabela com a nova coluna **")
print(df.head())

df.dropna() #remover os registros que contenham NA

print("\n** Mostrar a tabela sem os registros com NA **")
print(df)
