'''
  A necessidade deste script surgiu quando precisei consultar diariamente o valor do preço médio do Diesel no site da Petrobras 
e salvá-lo no banco de dados (Excluído do repositório esta parte)
  '''
'''
  The necessity of this code happened when I needed to consult every day the average diesel price in the Petrobras website 
  and save it in the database (dropped this part of the repository)
  '''
# Importar as bibliotecas necessárias
# Import the libraries that is necessary
from bs4 import BeautifulSoup
import requests

# Deixar o link do site em uma variável
# Let the weblink in a variable
url = 'https://precos.petrobras.com.br/seleção-de-estados-diesel'

# Espere 5 segundos pro site carregar
# Wait 5 seconds for the page load it
page = requests.get(url, timeout=5)

# Conectar no html da pagina
# Conect to the html
site = BeautifulSoup (page.text, "html.parser")
# o código deve retornos o status de 200, isso significa que nós conectamos com sucesso e tudo está em ordem
# The code returned us a status of 200, which means that we are successfully connected and everything is in order

# take the Div that contains our value
# Div que se encontra o valor
local_preco = site.find('div', attrs={'class': "quadrofinalcabecalho"})

# Local HTML que se encontra o preço do combustivel
# Place in the HTML that we can find the fuel price
preco_str = local_preco.find('h1', attrs={'id': 'telafinal-precofinal'})

# Recebeos o valor em formato de string
# the value come to us in string type

# Ajustes pra fazer o valor 'text' virar float e trocar a virgula por ponto
# adjustments to change string type to float type and replace the comma to dot
preco2 = preco_str.text
preco2 = preco2.replace(',', '.')
preco = float(preco2)

# Visualizar o resultado final
# See the final result
print(preco)
