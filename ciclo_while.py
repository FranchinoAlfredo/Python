# Importa il modulo 'random' per generare numeri casuali
import random

# Definizione della funzione principale per il gioco dell'indovina numero
def gioco_indovina_numero():
    # Genera un numero segreto casuale compreso tra 1 e 100
    numero_segreto = random.randint(1, 100)
    
    # Inizializza il conteggio dei tentativi e il flag per controllare se il numero è stato indovinato
    tentativi = 0
    indovinato = False

    # Stampa le istruzioni per l'utente
    print("Benvenuto al gioco dell'indovina numero!")
    print("Cercherai di indovinare il numero segreto compreso tra 1 e 100.")

    # Inizia il ciclo while che continuerà fino a quando il numero segreto non viene indovinato
    while not indovinato:
        # Chiedi all'utente di inserire un numero
        tentativo = int(input("Inserisci un numero: "))
        
        # Incrementa il conteggio dei tentativi
        tentativi += 1

        # Controlla se il numero inserito è uguale al numero segreto
        if tentativo == numero_segreto:
            indovinato = True
            print(f"Complimenti! Hai indovinato il numero segreto {numero_segreto} in {tentativi} tentativi.")
        # Se il numero è troppo basso, fornisce un suggerimento
        elif tentativo < numero_segreto:
            print("Il numero inserito è troppo basso. Prova di nuovo.")
        # Se il numero è troppo alto, fornisce un suggerimento
        else:
            print("Il numero inserito è troppo alto. Prova di nuovo.")

    # Messaggio finale una volta che il numero segreto è stato indovinato
    print("Fine del gioco.")

# Chiamiamo la funzione per avviare il gioco
gioco_indovina_numero()
