# Definizione della classe base "Veicolo"
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def info(self):
        return f"Veicolo: {self.marca} {self.modello}"


# Definizione della classe derivata "Auto" che eredita da "Veicolo"
class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        # Chiamiamo il costruttore della classe base usando super()
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    # Sovrascrittura del metodo info della classe base
    def info(self):
        return f"Auto: {self.marca} {self.modello}, Porte: {self.numero_porte}"


# Definizione della classe derivata "Moto" che eredita da "Veicolo"
class Moto(Veicolo):
    def __init__(self, marca, modello, tipo_guida):
        # Chiamiamo il costruttore della classe base usando super()
        super().__init__(marca, modello)
        self.tipo_guida = tipo_guida

    # Sovrascrittura del metodo info della classe base
    def info(self):
        return f"Moto: {self.marca} {self.modello}, Tipo di guida: {self.tipo_guida}"


# Creazione di istanze delle classi
auto1 = Auto("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CBR500R", "Sportiva")

# Accesso alle informazioni tramite i metodi delle classi
print(auto1.info())  # Output: Auto: Toyota Corolla, Porte: 4
print(moto1.info())  # Output: Moto: Honda CBR500R, Tipo di guida: Sportiva
