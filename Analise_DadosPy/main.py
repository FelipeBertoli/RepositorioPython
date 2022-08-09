import pandas as pd
import plotly.express as px

table = pd.read_csv("users.csv")

# 1. Visualizar a base de dados
table = table.drop("Unnamed: 0", axis=1)

# 2. Análise dos motivos do cancelamento
for column in table.columns:
        i = int(i + 1)
        graph = px.histogram(table, x=column, color="Churn", color_discrete_sequence=["red", "green"], text_auto=True)
        graph.write_image("output/graph" + str(i) + ".png") 
        print("-> GRÁFICO GERADO!")
