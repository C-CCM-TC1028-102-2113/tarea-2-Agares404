def main():
    #escribe tu código abajo de esta línea
    print("El mayor de tres números")
    a=int(input("Introduzca el primer número: "))
    b=int(input("Introduzca el segundo número: "))
    c=int(input("Introduzca el tercer número: "))

    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif  c > a and c > b:
        print(c)
    else:
        print("Alguno de los valores son iguales")
    pass


if __name__=='__main__':
    main()
