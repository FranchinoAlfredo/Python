# File: deploy_app.py

# Questo è il nostro file principale dell'applicazione

def main():
    print("Benvenuto nell'applicazione di esempio!")

if __name__ == "__main__":
    main()

# Fine di app.py

# ----------------------------------------

# Inizio di Dockerfile

# Usiamo un'immagine di base leggera di Python
FROM python:3.8-slim

# Impostiamo il working directory nell'immagine del container
WORKDIR /app

# Copiamo i file dell'applicazione nella directory del container
COPY deploy_app.py /app/

# Installiamo le dipendenze dell'applicazione (nel nostro caso non ne abbiamo)
# RUN pip install -r requirements.txt

# Definiamo il comando da eseguire quando il container viene avviato
CMD ["python", "deploy_app.py"]

# Fine di Dockerfile
