#automatizzare la copia di file da una cartella di origine a una cartella di destinazione

import os
import shutil

def automatizza_copia_file(cartella_origine, cartella_destinazione):
    try:
        # Verifica se la cartella di destinazione esiste, altrimenti creala
        if not os.path.exists(cartella_destinazione):
            os.makedirs(cartella_destinazione)

        # Ottieni la lista dei file nella cartella di origine
        elenco_file = os.listdir(cartella_origine)

        # Loop attraverso i file e copiali nella cartella di destinazione
        for file in elenco_file:
            percorso_file_origine = os.path.join(cartella_origine, file)
            percorso_file_destinazione = os.path.join(cartella_destinazione, file)
            shutil.copy2(percorso_file_origine, percorso_file_destinazione)
            print(f"Copiato il file: {file}")

        print("Automazione completata con successo!")

    except Exception as e:
        print(f"Si è verificato un errore durante l'automazione: {e}")

# Esempio di utilizzo
cartella_origine = "percorso/della/cartella/origine"
cartella_destinazione = "percorso/della/cartella/destinazione"

automatizza_copia_file(cartella_origine, cartella_destinazione)