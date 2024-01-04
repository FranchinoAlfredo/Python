# Importa il modulo 'venv' per la gestione degli ambienti virtuali
import venv
import os

# Definisci il percorso in cui desideri creare l'ambiente virtuale
virtualenv_path = os.path.join(os.getcwd(), 'my_virtual_environment')

# Crea un nuovo ambiente virtuale nella directory specificata
venv.create(virtualenv_path, clear=True)

# Stampa un messaggio informativo
print(f"Ambiente virtuale creato in {virtualenv_path}")

# Attiva l'ambiente virtuale (questa parte potrebbe variare a seconda del sistema operativo)
if os.name == 'posix':  # Per sistemi operativi basati su Unix (Linux, macOS)
    activate_script = os.path.join(virtualenv_path, 'bin', 'activate')
    activate_command = f"source {activate_script}"
elif os.name == 'nt':   # Per sistemi operativi Windows
    activate_script = os.path.join(virtualenv_path, 'Scripts', 'activate')
    activate_command = f"{activate_script}"

# Esegui il comando per attivare l'ambiente virtuale
os.system(activate_command)
print("Ambiente virtuale attivato")

# Ora puoi installare le dipendenze del tuo progetto all'interno dell'ambiente virtuale
# Ad esempio, installiamo la libreria 'requests' come dipendenza di esempio
os.system("pip install requests")

# Stampa un messaggio informativo
print("Dipendenze installate nell'ambiente virtuale")

# Quando hai finito di lavorare con l'ambiente virtuale, puoi disattivarlo
os.system("deactivate")

# Stampa un messaggio informativo
print("Ambiente virtuale disattivato")
