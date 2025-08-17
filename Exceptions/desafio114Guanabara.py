import requests

url = "https://www.pudim.com.br/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Consegui acessar o site do Pudim!")
except requests.exceptions.RequestException as e:
    print("Não consegui acessar o site do Pudim. Tente novamente mais tarde.")