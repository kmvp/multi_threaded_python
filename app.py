from hilo import userInput, cuadrado

if __name__ == '__main__':
    h1 = userInput()
    h2 = cuadrado()

    h1.start()
    h2.start()

    h1.join()
    h2.join()

    print("Programa terminado")