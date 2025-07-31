def MCD(numero1, numero2):
    if numero1 == 0:
        return numero2
    if numero2 == 0:
        return numero1
    else:
        resultado = numero1 % numero2
        resultado2 = numero2 % numero1
        return MCD(resultado, resultado2)
def repetitiva(palabra1, veces):
    if veces == 1:
        return palabra1
    else:
        resultado = repetitiva(palabra1, veces - 1)
        return  resultado + repetitiva(palabra1, veces - 1)



print("Parcial parte 2")
opcion = 0

while opcion != 6:
    print("Bienvenidos a esta parte del parcial")
    print("1.- Calcular el MCD de dos números")
    print("2.- Crear una cadena repetitiva N veces")
    print("3.- Contar cuántas veces aparece una letra en una cadena")
    print("4.- Convertir un numero decimal a binario")
    print("5.- Calcular cuantos dígitos tiene un numero")
    opcion = int(input("Ingrese la opcion que desea"))
    match opcion:
        case 1:
            print("\n Calcular el MCD de dos numeros")
            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
            print("El resultado es: ", MCD(numero1, numero2))
        case 2:
            print("\n crear una cadena repetitiva N veces")
            palabra1 = input("Ingrese la palabra: ")
            veces = int(input("Ingrese el numero de veces: "))
            print("La palabra es: ", repetitiva(palabra1, veces))


