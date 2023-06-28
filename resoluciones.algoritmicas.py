opcionn = 0

while opcionn != "5":
    print("---------------------------------------------------")
    print("| MENU DE OPCIONES |")
    print("1. Contar el número de ocurrencias de letras del alfabeto en una frase ingresada por el usuario")
    print("2. Solicitar números enteros y determinar si son negativos, positivos o iguales a cero")
    print("3. Suma y promedio de los valores de una lista")
    print("4. Suma de todos sus dígitos")
    print("5. Salir")
    print("---------------------------------------------------")
    print("")

    opcionn = input("Ingrese una opción: ")

    if opcionn == "1":
        frase = input("Ingresa una frase: ")
        frase = frase.lower()

        diccionario = {}

        for letra in frase:
            if letra.isalpha():
                if letra in diccionario:
                    diccionario[letra] += 1
                else:
                    diccionario[letra] = 1

        for letra in diccionario:
            print("La letra", letra, "aparece", diccionario[letra], "veces en la frase")

    elif opcionn == "2":
        numero = input("Ingrese un número entero, si desea finalizar ingrese * (asterisco): ")

        while numero != "*":
            numero = int(numero)

            if numero > 0:
                print("Número positivo")
            elif numero < 0:
                print("Número negativo")
            else:
                print("Número igual a cero")

            numero = input("Ingrese un número entero, si desea finalizar ingrese * (asterisco): ")

    elif opcionn == "3":
        lista = []
        numero = int(input("Ingrese números o 0 para finalizar: "))

        while numero != 0:
            lista.append(numero)
            numero = int(input(""))

            if numero == 0:
                break

        suma = sum(lista)
        promedio = suma / len(lista)
        print(f"Sumatoria: {suma} | Promedio: {promedio}")

    elif opcionn == "4":
        suma = 0
    numero = int(input("Ingrese un número entero o 0 para finalizar: "))

    while numero != 0:
        digito = numero % 10
        suma += digito
        
    print("La suma de los dígitos es:", suma)
