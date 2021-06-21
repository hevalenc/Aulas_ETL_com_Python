import pandas as pd
import pandera as pa

df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)

print("\n** Mostrar as primeiras 10 linhas da tabela **")
print(df.head(10))

print("\n** Mostrar as últimas 10 linhas da tabela **")
print(df.tail(10))

schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_length(2,2)),
        "ocorrencia_aerodromo": pa.Column(pa.String),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Int)
    }
)
#expressão regular (r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])?$') -> horas : minutos : segundos

print("\n** Validação dos dados da tabela com o pandera **")
print(schema.validate(df))

print("\n** Verificar os tipos dos dados **")
print(df.dtypes)

print("\n** Verificando os meses de cada registro **")
print(df.ocorrencia_dia.dt.month)
