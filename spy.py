import requests
from bs4 import BeautifulSoup

# URL de exemplo (troca pela que tu quiser)
url = "https://exemplo.com"

# Faz a requisição
response = requests.get(url)
response.raise_for_status()  # levanta erro se não der 200

# Cria o parser com BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Busca a div com id TESTEHTML
div = soup.find("div", {"id": "TESTEHTML"})

if div:
    print("Conteúdo da div TESTEHTML:")
    print(div.get_text(strip=True))
else:
    print("Div TESTEHTML não encontrada 😅")
