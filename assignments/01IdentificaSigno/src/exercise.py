import math
def main():
    #escribe tu código abajo de esta línea
    print("Identificar el signo")
    num=int(input("Dame un número: "))
    if num == 0:
        print("El número ingresado es cero")
    elif num < 0:
        print("El número ingresado es Negativo")
    else:
        print("El número ingresado es Positivo")
    pass
    

if __name__ == '__main__':
    main()
