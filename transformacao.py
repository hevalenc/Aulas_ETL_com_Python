import pandas as pd
import pandera as pa

valores_ausentes = ['**','###!','####','****','*****','NULL'] #referência dos valores a ser tratado no carregamento do arquivo, será exibido como NAN
df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)

print("\n** Mostrar as primeiras 10 linhas da tabela **")
print(df.head(10))

schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_length(2,2), nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Int)
    }
)

print("\n** Validação dos dados da tabela com o pandera **")
print(schema.validate(df))

print("\n** Verificar os tipos dos dados **")
print(df.dtypes)

print("\n** Mostrar o registro na posição 1 **")
print(df.loc[1]) #localizar por label

print("\n** Mostrar o registro na posição 1 **")
print(df.iloc[1]) #localizar pelo índice

print("\n** Mostrar o registro na última posição **")
print(df.iloc[-1]) #localizar pelo índice -1, retornará a última posição. Não é válido para 'loc'

print("\n** Mostrar as últimas linhas da tabela **")
print(df.tail())

print("\n** Mostrar os registros no entre as posições 10 à 14 **")
print(df.iloc[10:15])

print("\n** Mostrar os registros no entre as posições 10 à 15 **")
print(df.loc[10:15])

print("\n** Mostrar todos os dados da coluna 'ocorrencia_uf' **")
print(df.loc[:,'ocorrencia_uf'])

print("\n** Mostrar todos os dados da coluna 'ocorrencia_uf' **")
print(df['ocorrencia_uf'])

print("\n** Contar o total de dados com NA **")
print(df.isna().sum())

print("\n** Contar o total de dados com NULL **")
print(df.isnull().sum())

filtro = df.ocorrencia_uf.isnull()
print("\n** Mostrar os registros preenchidos com NULL na coluna 'ocorrencia_uf' **")
print(df.loc[filtro])

filtro = df.ocorrencia_aerodromo.isnull()
print("\n** Mostrar os registros preenchidos com NULL na coluna 'ocorrencia_aerodromo' **")
print(df.loc[filtro])

filtro = df.ocorrencia_hora.isnull()
print("\n** Mostrar os registros preenchidos com NULL na coluna 'ocorrencia_hora' **")
print(df.loc[filtro])

print("\n** Mostrar a quantidade de dados registrados em cada coluna **")
print(df.count())

filtro = df.total_recomendacoes > 10
print("\n** Mostrar os registros com mais de 10 recomendações na coluna 'recomendacoes' **")
print(df.loc[filtro])

filtro = df.total_recomendacoes > 10
print("\n** Mostrar os registros nas colunas 'ocorrencia_cidade' e 'total_recomendacoes'com mais de 10 recomendações na coluna 'recomendacoes' **")
print(df.loc[filtro, ['ocorrencia_cidade', 'total_recomendacoes']])

filtro = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'
print("\n** Mostrar os registros com cuja classificação == INCIDENTE GRAVE na coluna 'ocorrencia_classificacao' **")
print(df.loc[filtro])

filtro1 = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'
filtro2 = df.ocorrencia_uf == 'SP'
print("\n** Mostrar os registros cuja classificação == INCIDENTE GRAVE e o estado == SP nas colunas 'ocorrencia_classificacao' e 'ocorrencia_uf' **")
print(df.loc[filtro1 & filtro2])

filtro1 = df.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE'])
filtro2 = df.ocorrencia_uf == 'SP'
print("\n** Mostrar os registros cuja (classificação == INCIDENTE GRAVE ou classificação == INCIDENTE) e o estado == SP **")
print(df.loc[filtro1 & filtro2])

filtro = df.ocorrencia_cidade.str[0] == 'C'
print("\n** Mostrar os registros com cuja cidade começa com a letra C **")
print(df.loc[filtro])

filtro = df.ocorrencia_cidade.str[-1] == 'A'
print("\n** Mostrar os registros com cuja cidade termina com a letra A **")
print(df.loc[filtro])

filtro = df.ocorrencia_cidade.str[-2:] == 'MA'
print("\n** Mostrar os registros com cuja cidade termina com as letras MA **")
print(df.loc[filtro])

filtro = df.ocorrencia_cidade.str.contains('MA|AL')
print("\n** Mostrar os registros com cuja cidade contém (em qualquer parte do conteúdo) os caracteres MA ou AL **")
print(df.loc[filtro])

filtro = df.ocorrencia_dia.dt.year == 2015
print("\n** Mostrar os registros do ano de 2015 **")
print(df.loc[filtro])

filtro_ano = df.ocorrencia_dia.dt.year == 2015
filtro_mes = df.ocorrencia_dia.dt.month == 12
filtro_dia_inicio = df.ocorrencia_dia.dt.day > 2
filtro_dia_fim = df.ocorrencia_dia.dt.day < 9
print("\n** Mostrar os registros do ano de 2015 e mês 12 e dias entre 3 e 8 **")
print(df.loc[filtro_ano & filtro_mes & filtro_dia_inicio & filtro_dia_fim])

#filtro1 = df.ocorrencia_dia_hora >= '2015-12-03 11:00:00'
#filtro2 = df.ocorrencia_dia_hora <= '2015-12-08 14:30:00'
print("\n** Mostrar os registros na data '2015-12-03 11:00:00' e '2015-12-08 14:30:00' **")
#print(df.loc[filtro1 & filtro2])

filtro1 = df.ocorrencia_dia.dt.year == 2015
filtro2 = df.ocorrencia_dia.dt.month == 3
df201503 = df.loc[filtro1 & filtro2]
print("\n** Mostrar os registros do ano de 2015 e mês 03 **")
print(df201503)

print("\n** Mostrar a quantidade de cada tipo de dado registrado na coluna 'ocorrencia_classificacao' com 'codigo_ocorrencia' em 03/2015 **")
print(df201503.groupby(['ocorrencia_classificacao']).codigo_ocorrencia.count())

print("\n** Mostrar a quantidade de cada tipo de dado registrado na coluna 'ocorrencia_classificacao' com 'ocorrencia_aerodromo' em 03/2015 **")
print(df201503.groupby(['ocorrencia_classificacao']).ocorrencia_aerodromo.count())

print("\n** Mostrar os registros do ano de 2015 e mês 03, ordenado pelo tamanho da string **")
print(df201503.groupby(['ocorrencia_classificacao']).size())

print("\n** Mostrar os registros do ano de 2015 e mês 03, ordenado pelo valor do menor para o maior **")
print(df201503.groupby(['ocorrencia_classificacao']).size().sort_values())

print("\n** Mostrar os registros do ano de 2015 e mês 03, ordenado pelo valor do maior para o menor **")
print(df201503.groupby(['ocorrencia_classificacao']).size().sort_values(ascending=False))

filtro1 = df.ocorrencia_dia.dt.year == 2010
filtro2 = df.ocorrencia_uf.isin(['SP','MG','ES','RJ'])
dfsudeste2010 = df.loc[filtro1 & filtro2]
print("\n** Mostrar os dados de 2010 nos seguintes estados: 'SP','MG','ES','RJ' **")
print(dfsudeste2010)

print("\n** Mostrar os dados de 2010, na coluna 'ocorrencia_classificacao', nos seguintes estados: 'SP','MG','ES','RJ' **")
print(dfsudeste2010.groupby(['ocorrencia_classificacao']).size())

print("\n** Mostrar os dados de 2010, quantidade em cada coluna, nos seguintes estados: 'SP','MG','ES','RJ' **")
print(dfsudeste2010.count())

print("\n** Mostrar os dados de 2010, na coluna 'ocorrencia_classificacao', nos seguintes estados: 'SP','MG','ES','RJ' **")
print(dfsudeste2010.groupby(['ocorrencia_uf', 'ocorrencia_classificacao']).size())

print("\n** Mostrar os dados de 2010, quantidade em cada coluna, por cidade **")
print(dfsudeste2010.groupby(['ocorrencia_cidade']).size().sort_values(ascending=False))

filtro1 = dfsudeste2010.ocorrencia_cidade == 'RIO DE JANEIRO'
filtro2 = dfsudeste2010.total_recomendacoes > 0
print("\n** Mostrar os dados de 2010 da cidade do Rio de Janeiro **")
print(dfsudeste2010.loc[filtro1 & filtro2])

filtro = dfsudeste2010.ocorrencia_cidade == 'RIO DE JANEIRO'
print("\n** Valor total de recomendações da cidade do Rio de Janeiro em 2010 **")
print(dfsudeste2010.loc[filtro].total_recomendacoes.sum())

print("\n** Valor total de recomendações por aeroporto no sudeste em 2010 **")
print(dfsudeste2010.groupby(['ocorrencia_aerodromo'], dropna=False).total_recomendacoes.sum())

print("\n** Valor total de recomendações por cidade no sudeste em 2010 **")
print(dfsudeste2010.groupby(['ocorrencia_cidade']).total_recomendacoes.sum())

filtro = dfsudeste2010.total_recomendacoes > 0
print("\n** Valor total de recomendações, maior que 0, por cidade no sudeste em 2010 **")
print(dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade']).total_recomendacoes.sum().sort_values())

print("\n** Valor total de recomendações, maior que 0, por cidade e data no sudeste em 2010 **")
print(dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade', dfsudeste2010.ocorrencia_dia.dt.month]).total_recomendacoes.sum())

filtro1 = dfsudeste2010.total_recomendacoes > 0
filtro2 = dfsudeste2010.ocorrencia_cidade == 'SÃO PAULO'
print("\n")
print(dfsudeste2010.loc[filtro1 & filtro2])
