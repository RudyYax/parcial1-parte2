from unittest import result


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
        return  palabra1 + repetitiva(palabra1, veces - 1)

def contar(cadena, letra):
    if letra in cadena:
        return cadena.count(letra)

def Calcular(digitos):
    if digitos < 10:
        return digitos
    else:
        return 1 + Calcular(digitos // 10)

def Binario(NumeroBinario):
    if NumeroBinario == 0:
        return ''
    else:
        a = NumeroBinario // 2
        b = NumeroBinario % 2
        resultado = a +b
        return Binario(resultado)




print("Parcial parte 2")
opcion = 0

while opcion != 6:
    print("\n Bienvenidos a esta parte del parcial")
    print("1.- Calcular el MCD de dos números")
    print("2.- Crear una cadena repetitiva N veces")
    print("3.- Contar cuántas veces aparece una letra en una cadena")
    print("4.- Convertir un numero decimal a binario")
    print("5.- Calcular cuantos dígitos tiene un numero")
    print("6.- Salir del programa")
    opcion = int(input("Ingrese la opcion que desea: "))
    match opcion:
        case 1:
            print("\n Calcular el MCD de dos numeros")
            numero1 = int(input("Ingrese el primer numero: "))
            if numero1 <= 0:
                print("el numero no puede ser negativo")
                break
            else:
                numero2 = int(input("Ingrese el segundo numero: "))
                if numero2 <= 0:
                    print("el numero no puede ser negativo")
                    break
                else:
                    print("El MCD(Maximo Común Divisor es: ", MCD(numero1, numero2))
        case 2:
            print("\n crear una cadena repetitiva N veces")
            palabra1 = input("Ingrese la palabra: ")
            veces = int(input("Ingrese el numero de veces: "))
            if veces < 0:
                print("el numero no puede ser negativo")
                break
            else:
                print("La palabra es: ", repetitiva(palabra1, veces))
        case 3:
            print("\n Contar cuantas veces aparece una letra en una cadena")
            cadena = input("Ingrese una palabra: ")
            letra = input("Ingrese la letra que desea ver cuantas veces se repite: ")
            print(f"La letra {letra} aparece ", contar(cadena, letra))
        case 4:
            print("\n Convertir un numero decimal a binario")
            Numerobinario = int(input("Ingrese el numero de binario: "))
            print("El numero binario es: ", Binario(Numerobinario))

        case 5:
            print("Calcular cuantos digitos tiene un numero")
            digitos = int(input("Ingrese un numero: "))
            if digitos < 0:
                print("el numero no puede ser negativo")
            else:
                print(f"El numero {digitos} digitos tiene", Calcular(digitos), "Digitos")
        case 6:
            print("Gracias por utilizar nuestro programa :)")




