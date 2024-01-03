import requests
from bs4 import BeautifulSoup

# Funzione per ottenere dati da un'API esterna
def get_data_from_api():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # Effettua una richiesta GET all'API
    response = requests.get(api_url)
    
    # Verifica che la richiesta sia stata eseguita con successo (status code 200)
    if response.status_code == 200:
        # Converte la risposta in formato JSON
        data = response.json()
        print("Dati dall'API:")
        print(data)
    else:
        print("Errore nella richiesta all'API")

# Funzione per fare scraping di dati da una pagina web
def scrape_data_from_web():
    web_url = "https://example.com"
    
    # Effettua una richiesta GET alla pagina web
    response = requests.get(web_url)
    
    # Verifica che la richiesta sia stata eseguita con successo (status code 200)
    if response.status_code == 200:
        # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Esempio: Estrai il titolo della pagina
        title = soup.title.string
        print("Titolo della pagina web:")
        print(title)
    else:
        print("Errore nella richiesta alla pagina web")

# Esegui le funzioni
get_data_from_api()
scrape_data_from_web()
