
def main():
    #Escribe tu código debajo de esta línea
    print("Licencia de conducir")
    edad=int(input("Introduzca su edad: "))
    ide=input("¿Tiene identificación oficial? responda 's' para si y 'n' para no: ")

    if edad >= 18 and ide == 's':
        print("Trámite de licencia concedido")
    elif edad < 18 and edad > 0 or ide == 'n':
        print("No cumples los requisitos")
    elif ide != 's' or ide != 'n':
        print("Respuesa incorrecta")
    elif edad < 0:
        print("Respuesa incorrecta")


    pass


if __name__ == '__main__':
    main()
