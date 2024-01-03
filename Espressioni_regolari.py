import re

def formato_numero_telefono(numero):
    # Definiamo un modello di espressione regolare per i numeri di telefono
    # nel formato (XXX) XXX-XXXX
    pattern = re.compile(r'(\d{3})[.-]?(\d{3})[.-]?(\d{4})')

    # Cerchiamo il numero di telefono nel testo
    match = pattern.search(numero)

    if match:
        # Se troviamo una corrispondenza, formattiamo il numero nel nuovo formato
        numero_formattato = '({}) {}-{}'.format(match.group(1), match.group(2), match.group(3))
        return numero_formattato
    else:
        # Se non troviamo una corrispondenza, restituiamo il numero originale
        return "Formato non valido"

def main():
    # Testiamo la funzione con un esempio di testo contenente un numero di telefono
    testo = "Il mio numero di telefono è 123-456-7890."
    numero_formattato = formato_numero_telefono(testo)

    # Stampiamo i risultati
    print("Testo originale:", testo)
    print("Numero formattato:", numero_formattato)

if __name__ == "__main__":
    main()
