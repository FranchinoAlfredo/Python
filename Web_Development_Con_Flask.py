# Importa la classe Flask dal modulo flask
from flask import Flask

# Crea un'istanza di Flask
app = Flask(__name__)

# Definisci una route (URL) per la homepage
@app.route('/')
def home():
    return 'Benvenuto nella pagina principale!'

# Definisci un'altra route per una pagina di informazioni
@app.route('/info')
def info():
    return 'Questa è una pagina di informazioni.'

# Definisci la route con un parametro dinamico
@app.route('/utente/<nome>')
def saluta_utente(nome):
    return f'Ciao, {nome}!'

# Avvia l'applicazione se questo script viene eseguito direttamente
if __name__ == '__main__':
    # Imposta la modalità di debug per semplificare lo sviluppo
    app.debug = True
    # Avvia l'applicazione sulla porta 5000
    app.run()
