# Esercizio: Verifica della maggiore età

# Chiedi all'utente di inserire la propria età
eta = int(input("Inserisci la tua età: "))

# Verifica se l'utente è maggiorenne
if eta >= 18:
    # Se l'età è maggiore o uguale a 18, stampa un messaggio positivo
    print("Sei maggiorenne! Puoi accedere al contenuto per adulti.")
else:
    # Altrimenti, stampa un messaggio negativo
    print("Sei minorenne. L'accesso al contenuto per adulti è vietato.")

# Fine dell'esercizio
