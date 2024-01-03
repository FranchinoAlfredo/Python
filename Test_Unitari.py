import unittest

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


# Classe per i test unitari
class TestVeicoli(unittest.TestCase):
    def test_info_veicolo(self):
        veicolo = Veicolo("Ford", "Focus")
        self.assertEqual(veicolo.info(), "Veicolo: Ford Focus")

    def test_info_auto(self):
        auto = Auto("Toyota", "Corolla", 4)
        self.assertEqual(auto.info(), "Auto: Toyota Corolla, Porte: 4")

    def test_info_moto(self):
        moto = Moto("Honda", "CBR500R", "Sportiva")
        self.assertEqual(moto.info(), "Moto: Honda CBR500R, Tipo di guida: Sportiva")


# Eseguire i test unitari
if __name__ == "__main__":
    unittest.main()
