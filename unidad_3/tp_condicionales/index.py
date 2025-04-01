import random
import datetime
from statistics import mode, median, mean, StatisticsError

def actividad_1():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        break

    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

def actividad_2():
    while True:
        try:
            nota = float(input("Ingrese su nota (0-10): "))
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 0 y 10.")
            continue
        break
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def actividad_3():
    while True:
        try:
            numero = int(input("Ingrese un número par: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        if numero % 2 == 0:
            print("Ha ingresado un número par.")
            break
        else:
            print("Por favor, ingrese un número par.")

def actividad_4():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        break
    if edad < 12:
        categoria = "Niño/a"
    elif edad < 18:
        categoria = "Adolescente"
    elif edad < 30:
        categoria = "Adulto/a joven"
    else:
        categoria = "Adulto/a"
    print(f"Categoría: {categoria}")

def actividad_5():
    while True:
        password = input("Ingrese una contraseña (8-14 caracteres): ").strip()
        if 8 <= len(password) <= 14:
            print("Ha ingresado una contraseña correcta.")
            break
        else:
            print("La contraseña debe tener entre 8 y 14 caracteres.")

def actividad_6():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    print (f"Lista de números aleatorios: {numeros_aleatorios}")

    try:
        valor_moda = mode(numeros_aleatorios)
    except StatisticsError:
        valor_moda = None
        print("No se pudo determinar una moda única para la lista.")

    valor_mediana = median(numeros_aleatorios)
    valor_media = mean(numeros_aleatorios)

    print(f"Media: {valor_media}")
    print(f"Mediana: {valor_mediana}")
    if valor_moda is not None:
        print(f"Moda: {valor_moda}")
    else:
        print("Moda: No definida.")

    if valor_moda is None:
        print("No se puede determinar el sesgo por la falta de una moda única.")
    else:
        if valor_media > valor_mediana and valor_mediana > valor_moda:
            sesgo = "Sesgo positivo (a la derecha)"
        elif valor_media < valor_mediana and valor_mediana < valor_moda:
            sesgo = "Sesgo negativo (a la izquierda)"
        elif valor_media == valor_mediana == valor_moda:
            sesgo = "Sin sesgo"
        else:
            sesgo = "No se cumple ninguna de las condiciones de sesgo definidas"
        print(f"Resultado del análisis de sesgo: {sesgo}")

def actividad_7():
    texto = input("Ingrese una frase o palabra: ").strip()
    if not texto:
        print("No se ingresó ningún texto.")
        return
    
    if texto[-1].lower() in "aeiou":
        texto += "!"
    print(f"Resultado: {texto}")

def actividad_8():
    nombre = input("Ingrese su nombre: ").strip()
    if not nombre:
        print("No se ingresó ningún nombre válido.")
        return
    while True:
        opcion = input("Seleccione una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ").strip()
        if opcion not in ["1", "2", "3"]:
            print("Opción no válida. Intente de nuevo.")
        else:
            break
    if opcion == "1":
        resultado = nombre.upper()
    elif opcion == "2":
        resultado = nombre.lower()
    else:
        resultado = nombre.capitalize()
    print(f"Resultado: {resultado}")

def actividad_9():
    while True:
        try:
            magnitud = float(input("Ingrese la magnitud del terremoto: "))
            if magnitud < 0:
                print("La magnitud no puede ser negativa. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue
        break
    if magnitud < 3:
        categoria = "Muy leve"
    elif magnitud < 4:
        categoria = "Leve"
    elif magnitud < 5:
        categoria = "Moderado"
    elif magnitud < 6:
        categoria = "Fuerte"
    elif magnitud < 7:
        categoria = "Muy fuerte"
    else:
        categoria = "Extremo"
    print(f"La magnitud {magnitud} corresponde a: {categoria}")

def actividad_10():
    hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ").strip().upper()
    while hemisferio not in ["N", "S"]:
        hemisferio = input("Entrada no válida. Ingrese el hemisferio (N para norte, S para sur): ").strip().upper()
    
    while True:
        try:
            mes = int(input("Ingrese el mes (1-12): "))
            if mes < 1 or mes > 12:
                print("Mes no válido. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 12.")
            continue
        break

    dias_por_mes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            if dia < 1 or dia > dias_por_mes[mes]:
                print(f"Día no válido para el mes {mes}. Intente de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        break

    fecha = datetime.date(2001, mes, dia)
    dia_del_anio = fecha.timetuple().tm_yday

    if hemisferio == "N":
        if dia_del_anio >= 355 or dia_del_anio <= 79:
            estacion = "Invierno"
        elif dia_del_anio <= 80 and dia_del_anio <= 171:
            estacion = "Primavera"
        elif dia_del_anio <= 172 and dia_del_anio <= 263:
            estacion = "Verano"
        elif 264 <= dia_del_anio <= 354:
            estacion = "Otoño"
    else:
        if dia_del_anio >= 355 or dia_del_anio <= 79:
            estacion = "Verano"
        elif dia_del_anio <= 80 and dia_del_anio <= 171:
            estacion = "Otoño"
        elif dia_del_anio <= 172 and dia_del_anio <= 263:
            estacion = "Invierno"
        elif 264 <= dia_del_anio <= 354:
            estacion = "Primavera"

    print(f"Según la fecha {dia}/{mes} y el hemisferio {hemisferio} la estación es: {estacion}.")

def main():
    while True:
        print("\nMenú de ejercicios:")
        print("1) Verificar si es mayor de edad")
        print("2) Calificar nota (Aprobado/Desaprobado)")
        print("3) Ingresar solo números pares")
        print("4) Categoría según edad")
        print("5) Validar contraseña (8-14 caracteres)")
        print("6) Análisis de sesgo en lista de números aleatorios")
        print("7) Añadir exclamación si termina con vocal")
        print("8) Transformar nombre según opción")
        print("9) Clasificar magnitud de terremoto")
        print("10) Determinar estación del año según fecha y hemisferio")
        print("0) Salir")

        opcion = input("Seleccione el ejercicio que desea ejecutar (0-10): ").strip()
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