import random

def actividad_1():
    """
    Imprime en pantalla todos los números enteros desde 0 hasta 100,
    en orden creciente, mostrando un número por línea.
    """
    print("\nEjercicio 1: Números del 0 al 100")
    for i in range(101):
        print(i)


def actividad_2():
    """
    Solicita al usuario un número entero y determina la cantidad
    de dígitos que contiene.
    """
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        break
    cantidad_digitos = len(str(abs(numero)))
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")


def actividad_3():
    """
    Pide dos valores enteros al usuario y suma todos los números enteros
    comprendidos entre ellos, excluyendo los dos extremos.
    """
    while True:
        try:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
        except ValueError:
            print("Entrada no válida. Ingrese dos números enteros.")
            continue
        break
    menor, mayor = min(valor1, valor2), max(valor1, valor2)
    suma = sum(range(menor + 1, mayor))
    print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma}")


def actividad_4():
    """
    Permite al usuario ingresar números enteros en secuencia y los suma.
    El proceso se detiene cuando se ingresa un 0, mostrando el total acumulado.
    """
    total = 0
    print("\nIngrese números enteros para sumarlos (ingrese 0 para terminar):")
    while True:
        try:
            numero = int(input("Número: "))
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue
        if numero == 0:
            break
        total += numero
    print(f"El total acumulado es: {total}")


def actividad_5():
    """
    Juego de adivinar un número aleatorio entre 0 y 9.
    Se indica al usuario cuántos intentos le tomó acertar.
    """
    numero_secreto = random.randint(0, 9)
    intentos = 0
    print("\nJuego: Adivina el número (entre 0 y 9)")
    while True:
        try:
            intento = int(input("Ingrese su intento: "))
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
            continue
        intentos += 1
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            break
        else:
            print("Número incorrecto, intenta de nuevo.")


def actividad_6():
    """
    Imprime en pantalla todos los números pares comprendidos entre 0 y 100,
    en orden decreciente.
    """
    print("\nEjercicio 6: Números pares del 100 al 0")
    # Se asume que 100 es par; se recorre desde 100 hasta 0 de dos en dos
    for i in range(100, -1, -2):
        print(i)


def actividad_7():
    """
    Solicita al usuario un número entero positivo y calcula la suma
    de todos los números enteros desde 0 hasta ese número.
    """
    while True:
        try:
            n = int(input("Ingrese un número entero positivo: "))
            if n < 0:
                print("El número debe ser positivo. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        break
    suma = sum(range(n + 1))
    print(f"La suma de los números desde 0 hasta {n} es: {suma}")


def actividad_8():
    """
    Permite al usuario ingresar 100 números enteros y cuenta:
      - Cantidad de números pares.
      - Cantidad de números impares.
      - Cantidad de números positivos.
      - Cantidad de números negativos.
    """
    cantidad = 100
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    print("\nIngrese 100 números enteros:")
    for i in range(cantidad):
        while True:
            try:
                num = int(input(f"Número {i+1}: "))
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
                continue
            break

        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1

    print("\nResultados:")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")


def actividad_9():
    """
    Permite al usuario ingresar 100 números enteros y calcula la media (promedio)
    de esos valores.
    """
    cantidad = 100
    suma = 0

    print("\nIngrese 100 números enteros para calcular la media:")
    for i in range(cantidad):
        while True:
            try:
                num = int(input(f"Número {i+1}: "))
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
                continue
            break
        suma += num

    media = suma / cantidad
    print(f"La media de los {cantidad} números ingresados es: {media}")


def actividad_10():
    """
    Pide al usuario un número y muestra en pantalla el mismo número con sus dígitos en orden inverso.
    Ejemplo: Si el usuario ingresa 547, se mostrará 745.
    """
    num_str = input("Ingrese un número: ").strip()
    if not num_str:
        print("No se ingresó ningún número.")
        return
    numero_invertido = num_str[::-1]
    print(f"El número invertido es: {numero_invertido}")


def main():
    while True:
        print("\nMenú de ejercicios de estructuras repetitivas:")
        print("1) Imprimir números del 0 al 100")
        print("2) Determinar la cantidad de dígitos de un número")
        print("3) Sumar números entre dos valores (excluyendo extremos)")
        print("4) Sumar números hasta ingresar 0")
        print("5) Juego: Adivinar número entre 0 y 9")
        print("6) Imprimir números pares del 100 al 0")
        print("7) Sumar números desde 0 hasta un entero positivo")
        print("8) Contar pares, impares, positivos y negativos de 100 números")
        print("9) Calcular la media de 100 números")
        print("10) Invertir el orden de los dígitos de un número")
        print("0) Salir")

        opcion = input("Seleccione la actividad que desea ejecutar (0-10): ").strip()
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion == "1":
            actividad_1()
        elif opcion == "2":
            actividad_2()
        elif opcion == "3":
            actividad_3()
        elif opcion == "4":
            actividad_4()
        elif opcion == "5":
            actividad_5()
        elif opcion == "6":
            actividad_6()
        elif opcion == "7":
            actividad_7()
        elif opcion == "8":
            actividad_8()
        elif opcion == "9":
            actividad_9()
        elif opcion == "10":
            actividad_10()
        else:
            print("Opción no válida. Intente de nuevo.")
        print("\n" + "="*40)


main()