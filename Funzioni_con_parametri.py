# Definiamo una funzione senza parametri
def saluta():
    print("Ciao! Benvenuto nella nostra applicazione.")

# Definiamo una funzione con parametri
def somma(a, b):
    risultato = a + b
    return risultato

# Funzione principale
def main():
    # Chiamiamo la funzione senza parametri
    saluta()

    # Chiediamo all'utente due numeri
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    # Chiamiamo la funzione con parametri e otteniamo il risultato
    risultato_somma = somma(num1, num2)

    # Stampiamo il risultato
    print(f"La somma di {num1} e {num2} è: {risultato_somma}")

# Chiamiamo la funzione principale per avviare il programma
main()
