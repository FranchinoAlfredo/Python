import threading
import time

# Funzione che simula un'attività svolta da un thread
def contatore(nome, limite):
    for i in range(1, limite + 1):
        print(f'Thread {nome}: Conteggio {i}')
        time.sleep(1)

# Creazione dei thread
thread1 = threading.Thread(target=contatore, args=('A', 5))
thread2 = threading.Thread(target=contatore, args=('B', 3))
thread3 = threading.Thread(target=contatore, args=('C', 4))

# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()

# Attendi che tutti i thread abbiano completato l'esecuzione
thread1.join()
thread2.join()
thread3.join()

print('Programma completato.')
