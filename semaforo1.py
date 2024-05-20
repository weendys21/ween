import threading
import time
#Crear un semaforo con un caracter inicial de 2
semaphore= threading.Semaphore(1)
def tarea(id):
    print(f"Tarea {id} intentando acceder al recurso")
    with semaphore:
	    print(f"tarea {id} ha adquirido el semáforo")
	    time.sleep(2)
	    print (f"Tarea {id} ha liberado el semáforo")
#Crear múltiples hilosque ejecutenla funcion "tarea"
threads =[]
for i in range(5):
    thread= threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()
#Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()
	
