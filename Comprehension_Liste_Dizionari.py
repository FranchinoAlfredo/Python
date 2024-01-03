# Comprehension di Liste
# Creare una lista dei quadrati dei numeri da 1 a 10
squares = [x**2 for x in range(1, 11)]

# Creare una lista dei numeri pari da 1 a 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# Comprehension di Dizionari
# Creare un dizionario con numeri come chiavi e i loro quadrati come valori
squares_dict = {x: x**2 for x in range(1, 6)}

# Filtrare un dizionario per mantenere solo le coppie chiave-valore con valori pari
even_squares_dict = {key: value for key, value in squares_dict.items() if value % 2 == 0}

# Stampa dei risultati
print("Lista dei quadrati:", squares)
print("Numeri pari da 1 a 20:", even_numbers)
print("Dizionario dei quadrati:", squares_dict)
print("Dizionario con quadrati pari:", even_squares_dict)
