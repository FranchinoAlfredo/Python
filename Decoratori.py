# Definiamo un decoratore che aggiunge un log prima e dopo l'esecuzione della funzione
def decoratore_log(funzione):
    def funzione_decorata(*args, **kwargs):
        # Operazioni prima dell'esecuzione della funzione
        print(f"Log: Prima di eseguire {funzione.__name__}")

        # Eseguiamo la funzione originale
        risultato = funzione(*args, **kwargs)

        # Operazioni dopo l'esecuzione della funzione
        print(f"Log: Dopo l'esecuzione di {funzione.__name__}")

        return risultato

    # Restituisci la funzione decorata
    return funzione_decorata

# Applichiamo il decoratore a una funzione
@decoratore_log
def saluta(nome):
    return f"Ciao, {nome}!"

def main():
    # Chiamiamo la funzione decorata
    risultato = saluta("Mario")

    # Stampiamo il risultato
    print("Risultato:", risultato)

if __name__ == "__main__":
    main()
