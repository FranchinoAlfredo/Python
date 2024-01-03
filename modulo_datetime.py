from datetime import datetime

def differenza_temporale(data_inizio, data_fine):
    # Calcoliamo la differenza di tempo tra le due date
    differenza = data_fine - data_inizio
    return differenza

def main():
    # Definiamo due date
    data_inizio = datetime(2022, 1, 1, 12, 0, 0)  # 1 gennaio 2022, ore 12:00:00
    data_fine = datetime.now()  # Data e ora correnti

    # Calcoliamo la differenza di tempo
    differenza = differenza_temporale(data_inizio, data_fine)

    # Stampiamo i risultati
    print("Data di inizio:", data_inizio)
    print("Data di fine:", data_fine)
    print("Differenza di tempo:", differenza)

    # Estraiamo i componenti della differenza di tempo
    giorni = differenza.days
    ore, resto = divmod(differenza.seconds, 3600)
    minuti, secondi = divmod(resto, 60)

    print(f"\nDifferenza dettagliata:")
    print(f"Giorni: {giorni}")
    print(f"Ore: {ore}")
    print(f"Minuti: {minuti}")
    print(f"Secondi: {secondi}")

if __name__ == "__main__":
    main()
