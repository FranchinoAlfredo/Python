# Importiamo un modulo Python predefinito
import math

# Funzione per calcolare l'area di un cerchio utilizzando il modulo math
def calcola_area_cerchio(raggio):
    area = math.pi * raggio**2
    return area

# Funzione principale
def main():
    # Utilizziamo il modulo math per calcolare l'area di un cerchio
    raggio_cerchio = float(input("Inserisci il raggio del cerchio: "))
    area_cerchio = calcola_area_cerchio(raggio_cerchio)
    print(f"L'area del cerchio con raggio {raggio_cerchio} è: {area_cerchio:.2f}")

    # Esploriamo una libreria di terze parti (in questo caso 'requests') per fare una richiesta HTTP
    try:
        # Importiamo la libreria di terze parti
        import requests

        # Facciamo una richiesta GET a un sito web
        response = requests.get("https://www.example.com")

        # Stampiamo lo status code della risposta
        print(f"Status code della richiesta HTTP: {response.status_code}")

    except ImportError:
        # Gestiamo l'eccezione se la libreria di terze parti non è installata
        print("Errore: La libreria 'requests' non è installata. Installala usando 'pip install requests'.")
    except Exception as e:
        # Gestiamo altri errori che potrebbero verificarsi durante la richiesta HTTP
        print(f"Errore durante la richiesta HTTP: {e}")

# Chiamiamo la funzione principale per avviare il programma
main()
