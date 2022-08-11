from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Passo 1. Pegar cotação do dólar
# -Abrir navegador
nav = webdriver.Chrome(r"C:\Users\user\chromedriver.exe")

# - Entrar no Google
nav.get("https://www.google.com.br/")

# - Pesquisar e pegar cotação do dólar
nav.find_element('xpath', 
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar")
nav.find_element('xpath', 
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dollar_price = nav.find_element('xpath', 
            '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print()
print("- COTAÇÃO DÓLAR: " + str(dollar_price))

# Passo 2. Pegar cotação do euro
# - Entrar no Google
nav.get("https://www.google.com.br/")

# - Pesquisar e pegar cotação do euro
nav.find_element('xpath', 
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro")
nav.find_element('xpath', 
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro_price = nav.find_element('xpath', 
            '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print("- COTAÇÃO EURO: " + str(euro_price))

# Passo 3. Pegar cotação do ouro
# - Entrar no site 
nav.get("https://www.melhorcambio.com/ouro-hoje")

# - Pegar cotação do ouro
gold_price = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
gold_price = gold_price.replace(",", ".")
print("- COTAÇÃO OURO: " + str(gold_price))

nav.quit()

# Passo 4. Atualizar base de dados
table = pd.read_excel(r"C:\Users\user\Documents\Projetos\Python\Automacao_WebPy\Produtos.xlsx")

# Passo 5. Recalcular base de dados
# - Atualizar as cotações 
table.loc[table["Moeda"] == "Dólar", "Cotação"] = float(dollar_price)
table.loc[table["Moeda"] == "Euro", "Cotação"] = float(euro_price)
table.loc[table["Moeda"] == "Ouro", "Cotação"] = float(gold_price)

# - Preço de Compra = Preço Original * Cotação
table["Preço de Compra"] = table["Preço Original"] * table["Cotação"]

# - Preço de Venda = Preço de Compra * Margem
table["Preço de Venda"] = table["Preço de Compra"] * table["Margem"]

# Passo 6. Exportar a base de dados
table.to_excel(r"C:\Users\user\Documents\Projetos\Python\Automacao_WebPy\Novos_Produtos.xlsx", index = False)
print("-> BASE DE DADOS GERADA!")