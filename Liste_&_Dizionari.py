# Esercizio: Gestione di una Lista e un Dizionario

# Creare una lista di numeri interi
numeri = [1, 2, 3, 4, 5]

# Stampa la lista originale
print("Lista originale:", numeri)

# Aggiungi un numero alla lista
numeri.append(6)

# Stampa la lista dopo l'aggiunta
print("Lista dopo l'aggiunta:", numeri)

# Accedi a un elemento specifico nella lista
primo_numero = numeri[0]
print("Primo numero nella lista:", primo_numero)

# Rimuovi un numero dalla lista
numeri.remove(3)

# Stampa la lista dopo la rimozione
print("Lista dopo la rimozione del numero 3:", numeri)

# Creare un dizionario con informazioni personali
informazioni_personali = {
    'nome': 'Mario',
    'cognome': 'Rossi',
    'età': 30,
    'professione': 'Ingegnere'
}

# Stampa il dizionario originale
print("\nDizionario originale:", informazioni_personali)

# Aggiungi una nuova chiave-valore al dizionario
informazioni_personali['città'] = 'Roma'

# Stampa il dizionario dopo l'aggiunta
print("Dizionario dopo l'aggiunta della città:", informazioni_personali)

# Accedi a un valore specifico nel dizionario
età_persona = informazioni_personali['età']
print("Età della persona nel dizionario:", età_persona)

# Rimuovi una chiave dal dizionario
del informazioni_personali['professione']

# Stampa il dizionario dopo la rimozione della chiave 'professione'
print("Dizionario dopo la rimozione della professione:", informazioni_personali)
