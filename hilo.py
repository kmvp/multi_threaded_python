from threading import Thread

import time

flag = True

class userInput(Thread):

    def run(self):
        print("Esperando un mensaje...")
        msg=input()
        global flag
        flag = False
        time.sleep(1)
        print("El mensaje fue: %s" %(msg))

class cuadrado(Thread):

    def run(self):
        global flag
        contador = 0
        while(flag):
            contador =  contador + 1
            print("Contador actual: %d" %(contador))
            time.sleep(0.9)
        print("Mientras escribías el cuadrado del valor %d fue calculado: %d" %(contador, contador**2))