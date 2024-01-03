# Funzione per scrivere dati in un file
def scrivi_su_file(nome_file, dati):
    try:
        with open(nome_file, 'w') as file:
            # Scriviamo i dati nel file
            file.write(dati)
        print(f"I dati sono stati scritti con successo nel file '{nome_file}'.")
    except Exception as e:
        # Gestiamo eventuali errori durante la scrittura
        print(f"Errore durante la scrittura nel file: {e}")

# Funzione per leggere dati da un file
def leggi_da_file(nome_file):
    try:
        with open(nome_file, 'r') as file:
            # Leggiamo i dati dal file
            dati = file.read()
            print(f"I dati letti dal file '{nome_file}':\n{dati}")
            return dati
    except FileNotFoundError:
        # Gestiamo l'eccezione se il file non esiste
        print(f"Errore: Il file '{nome_file}' non esiste.")
    except Exception as e:
        # Gestiamo altri errori durante la lettura
        print(f"Errore durante la lettura dal file: {e}")
    return None

# Funzione principale
def main():
    # Scriviamo dati in un file
    dati_da_scrivere = "Questi sono dati da scrivere in un file."
    nome_file_scrittura = "dati.txt"
    scrivi_su_file(nome_file_scrittura, dati_da_scrivere)

    # Leggiamo dati da un file
    nome_file_lettura = "dati.txt"
    dati_letti = leggi_da_file(nome_file_lettura)

    # Utilizziamo i dati letti (ad esempio, stampiamoli)
    if dati_letti is not None:
        print("Utilizziamo i dati letti:")
        print(dati_letti)

# Chiamiamo la funzione principale per avviare il programma
main()
