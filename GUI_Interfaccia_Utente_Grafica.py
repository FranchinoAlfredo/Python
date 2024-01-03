import tkinter as tk

def on_button_click():
    label.config(text="Cliccato il pulsante!")

# Creazione della finestra principale
app = tk.Tk()
app.title("Esempio GUI con Tkinter")

# Creazione di un pulsante
button = tk.Button(app, text="Clicca qui", command=on_button_click)
button.pack(pady=10)

# Creazione di una label
label = tk.Label(app, text="Benvenuto nella GUI!")
label.pack(pady=20)

# Avvio del ciclo principale dell'applicazione
app.mainloop()
