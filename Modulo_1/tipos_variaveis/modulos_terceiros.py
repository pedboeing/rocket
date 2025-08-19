print("\n Importação e uso de um módulo de terceiros")
import requests 

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação http para {url} retornou o status {response.status_code}")