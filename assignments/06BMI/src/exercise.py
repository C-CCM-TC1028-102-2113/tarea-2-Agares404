def main():
    #escribe tu código abajo de esta línea
    print("Ordena 3 numeros")
    p = float(input("Ingresa tu peso en kg: "))
    a = float(input("Ingresa tu altura en m: "))

    imc=p/(a*a)

    if imc < 20:
        print("PESO BAJO")
    elif imc >= 20 and imc < 25:
        print("NORMAL")
    elif imc >= 25 and imc < 30:
        print("SOBREPESO")
    elif imc >= 30 and imc < 40:
        print("OBESIDAD")
    elif imc >= 40:
        print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo")
    pass
if __name__=='__main__':
    main()
