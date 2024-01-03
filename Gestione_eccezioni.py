# Definiamo una funzione che divide due numeri e gestisce le eccezioni
def divisione_sicura(dividendo, divisore):
    try:
        risultato = dividendo / divisore
        return risultato
    except ZeroDivisionError:
        # Gestiamo l'eccezione quando il divisore è zero
        print("Errore: Impossibile dividere per zero.")
    except Exception as e:
        # Gestiamo altre eccezioni generiche
        print(f"Errore: {e}")
    finally:
        # Il blocco finally viene eseguito sempre, indipendentemente se si verifica un'eccezione o meno
        print("Operazione di divisione terminata.")

# Funzione principale
def main():
    # Chiediamo all'utente due numeri
    try:
        dividendo = float(input("Inserisci il dividendo: "))
        divisore = float(input("Inserisci il divisore: "))
        
        # Chiamiamo la funzione che può generare eccezioni
        risultato_divisione = divisione_sicura(dividendo, divisore)

        if risultato_divisione is not None:
            print(f"Il risultato della divisione è: {risultato_divisione}")

    except ValueError:
        # Gestiamo l'eccezione se l'utente inserisce un input non valido
        print("Errore: Inserisci numeri validi.")

# Chiamiamo la funzione principale per avviare il programma
main()
