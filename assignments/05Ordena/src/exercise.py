def main():
    # Escribe el código adecuado para completar el programa
    print("Ordena 3 numeros")
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if x > y and x > z and y > z:
        print(x,y,z)
    elif x > y and x > z and z > y:
        print(x,z,y)
    elif  y > x and y > z and x > z:
        print(y,x,z)
    elif  y > x and y > z and z > x:
        print(y,z,x)
    elif  z > x and z > y and x > y:
        print(z,x,y)
    else:
        print(z,y,x)
    pass


if __name__=='__main__':
    main()
