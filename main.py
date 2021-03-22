#!/usr/bin/python

import threading
import time

i = "@@@@@a!!!bc@@@@@@def$$$$$$gh!!!!!!ijkl1233312123mn222321opqr1233stuv67889xy&#$%z"

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global i
        print("Iniciando " + self.name)
        # pega o lock para sincroniar as threads
        threadLock.acquire()
        verifica_string(i)
        # libera o lock para as threads
        threadLock.release()

def verifica_string(string):
    global i
    print(i)
    for c in string:   
        if c.islower():
            i = string.replace(c, c.upper())
            time.sleep(1) 
            break


threadLock = threading.Lock()
threads = []

# cria as threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")
thread3 = myThread(3, "Thread-3")
thread4 = myThread(4, "Thread-4")
thread5 = myThread(5, "Thread-5")
thread6 = myThread(6, "Thread-6")
thread7 = myThread(7, "Thread-7")
thread8 = myThread(8, "Thread-8")
thread9 = myThread(9, "Thread-9")
thread10 = myThread(10, "Thread-10")
thread11 = myThread(11, "Thread-11")
thread12 = myThread(12, "Thread-12")
thread13 = myThread(13, "Thread-13")
thread14 = myThread(14, "Thread-14")
thread15 = myThread(15, "Thread-15")
thread16 = myThread(16, "Thread-16")
thread17 = myThread(17, "Thread-17")
thread18 = myThread(18, "Thread-18")
thread19 = myThread(19, "Thread-19")
thread20 = myThread(20, "Thread-20")
thread21 = myThread(21, "Thread-21")
thread22 = myThread(22, "Thread-22")
thread23 = myThread(23, "Thread-23")
thread24 = myThread(24, "Thread-24")
thread25 = myThread(25, "Thread-25")
thread26 = myThread(26, "Thread-26")
thread27 = myThread(27, "Thread-27")
thread28 = myThread(28, "Thread-28")
thread29 = myThread(29, "Thread-29")
thread30 = myThread(30, "Thread-30")

# inicia as threads

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()
thread30.start()

# adiciona os treads a lista

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
threads.append(thread6)
threads.append(thread7)
threads.append(thread8)
threads.append(thread9)
threads.append(thread10)
threads.append(thread11)
threads.append(thread12)
threads.append(thread13)
threads.append(thread14)
threads.append(thread15)
threads.append(thread16)
threads.append(thread17)
threads.append(thread18)
threads.append(thread19)
threads.append(thread20)
threads.append(thread21)
threads.append(thread22)
threads.append(thread23)
threads.append(thread24)
threads.append(thread25)
threads.append(thread26)
threads.append(thread27)
threads.append(thread28)
threads.append(thread29)
threads.append(thread30)

# Espera os threads acabarem
for t in threads:
    t.join()
print("finalizado")
print(i)
