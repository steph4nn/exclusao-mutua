
import threading
import time
from threading import Semaphore

numero = 0
mutex = Semaphore(1)


# Codigo estah pulando numeros, e repetindo numeros entre threads

def p1():
    global numero
    while True:
        global mutex    
        mutex.acquire()
        numero += 1
        mutex.release()
        print('P1:', numero)
        time.sleep(1)

def p2():
    global numero
    while True:
        global mutex
        mutex.acquire()
        numero += 1
        mutex.release()
        print('P2:', numero)
        time.sleep(1)


t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()

