import math

# --- Ejercicio 1 ---
def imprimir_hola_mundo():
    """Imprime 'Hola Mundo!'"""
    print("Hola Mundo!")

def correr_ejercicio1():
    imprimir_hola_mundo()


# --- Ejercicio 2 ---
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola {nombre}!"

def solicitar_nombre():
    """Solicita y devuelve el nombre del usuario."""
    return input("Ingrese su nombre: ")

def correr_ejercicio2():
    nombre = solicitar_nombre()
    saludo = saludar_usuario(nombre)
    print(saludo)


# --- Ejercicio 3 ---
def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime información personal en un formato específico."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def solicitar_informacion_personal():
    """Solicita al usuario los datos personales y los retorna."""
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    return nombre, apellido, edad, residencia

def correr_ejercicio3():
    datos = solicitar_informacion_personal()
    informacion_personal(*datos)


# --- Ejercicio 4 ---
def calcular_area_circulo(radio):
    """Calcula y retorna el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Calcula y retorna el perímetro de un círculo dado su radio."""
    return 2 * math.pi * radio

def solicitar_radio():
    """Solicita el radio al usuario y lo retorna (asegurándose de que sea un número)."""
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            return radio
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio4():
    radio = solicitar_radio()
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")


# --- Ejercicio 5 ---
def segundos_a_horas(segundos):
    """Convierte segundos a horas."""
    return segundos / 3600

def solicitar_segundos():
    """Solicita al usuario una cantidad de segundos y la retorna."""
    while True:
        try:
            segundos = int(input("Ingrese los segundos: "))
            return segundos
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio5():
    segundos = solicitar_segundos()
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")


# --- Ejercicio 6 ---
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar para el número dado, del 1 al 10."""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def solicitar_numero_tabla():
    """Solicita un número para imprimir su tabla de multiplicar."""
    while True:
        try:
            numero = int(input("Ingrese un número para su tabla de multiplicar: "))
            return numero
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio6():
    numero = solicitar_numero_tabla()
    tabla_multiplicar(numero)


# --- Ejercicio 7 ---
def operaciones_basicas(a, b):
    """Realiza operaciones básicas y retorna una tupla con (suma, resta, multiplicación, división)."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero"
    return (suma, resta, multiplicacion, division)

def solicitar_dos_numeros():
    """Solicita al usuario dos números y los retorna."""
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio7():
    a, b = solicitar_dos_numeros()
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")


# --- Ejercicio 8 ---
def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    if altura == 0:
        return None
    return peso / (altura ** 2)

def solicitar_datos_imc():
    """Solicita peso y altura al usuario y los retorna."""
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: "))
            altura = float(input("Ingrese su altura en metros: "))
            return peso, altura
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio8():
    peso, altura = solicitar_datos_imc()
    imc = calcular_imc(peso, altura)
    if imc is not None:
        print(f"Su IMC es: {imc:.2f}")
    else:
        print("No se puede calcular el IMC con una altura de 0.")


# --- Ejercicio 9 ---
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def solicitar_celsius():
    """Solicita una temperatura en °C y la retorna."""
    while True:
        try:
            celsius = float(input("Ingrese la temperatura en °C: "))
            return celsius
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio9():
    celsius = solicitar_celsius()
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C son {fahrenheit:.2f}°F")


# --- Ejercicio 10 ---
def calcular_promedio(a, b, c):
    """Calcula y retorna el promedio de tres números."""
    return (a + b + c) / 3

def solicitar_tres_numeros():
    """Solicita tres números y los retorna como una tupla."""
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            num3 = float(input("Ingrese el tercer número: "))
            return num1, num2, num3
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def correr_ejercicio10():
    num1, num2, num3 = solicitar_tres_numeros()
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio es: {promedio:.2f}")


# --- Menú principal ---
def main():
    while True:
        print("\nMenú del TP de funciones:")
        print("1) Imprimir 'Hola Mundo!'")
        print("2) Saludar al usuario")
        print("3) Mostrar información personal")
        print("4) Calcular área y perímetro de un círculo")
        print("5) Convertir segundos a horas")
        print("6) Mostrar tabla de multiplicar")
        print("7) Realizar operaciones básicas")
        print("8) Calcular el IMC")
        print("9) Convertir Celsius a Fahrenheit")
        print("10) Calcular promedio de tres números")
        print("0) Salir")
        
        opcion = input("Seleccione la actividad que desea ejecutar (0-10): ").strip()
        
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion == "1":
            correr_ejercicio1()
        elif opcion == "2":
            correr_ejercicio2()
        elif opcion == "3":
            correr_ejercicio3()
        elif opcion == "4":
            correr_ejercicio4()
        elif opcion == "5":
            correr_ejercicio5()
        elif opcion == "6":
            correr_ejercicio6()
        elif opcion == "7":
            correr_ejercicio7()
        elif opcion == "8":
            correr_ejercicio8()
        elif opcion == "9":
            correr_ejercicio9()
        elif opcion == "10":
            correr_ejercicio10()
        else:
            print("Opción no válida. Intente de nuevo.")
        print("\n" + "=" * 40)

main()