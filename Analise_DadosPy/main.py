import pandas as pd
import plotly

table = pd.read_csv("users.csv")

# 1. Visualizar a base de dados
table = table.drop("Unnamed: 0", axis=1)

# 2. Tratamento de erros
# - Valores que estão reconhecidos de forma errada
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")
print(table)

# - Valores vazios
# deletando as colunas vazias
table = table.dropna(how="all", axis=1)
# deletando as linhas vazias
table = table.dropna(how="any", axis=0)

# 3. Análise dos cancelamentos
print(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# 4. Análise dos motivos do cancelamento