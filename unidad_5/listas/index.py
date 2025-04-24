def listar_multiplos_de_4():
    mult4 = list(range(4, 101, 4))
    print("1) Múltiplos de 4 de 1 a 100:", mult4)

def mostrar_penultimo_elemento_favoritos():
    favoritos = ["chocolate", "música", "lectura", "cine", "programación"]
    print("2) Penúltimo elemento de favoritos:", favoritos[-2])

def crear_y_rellenar_lista_palabras():
    lista_vacia = []
    lista_vacia.append("hola")
    lista_vacia.append("mundo")
    lista_vacia.append("python")
    print("3) Lista vacía tras append:", lista_vacia)

def reemplazar_animales():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print("4) Lista 'animales' modificada:", animales)

# Este programa hace lo siguiente:
    # 1. Define una lista llamada "numeros" con los siguientes valores: 8, 15, 3, 22, 7.
    # 2. Utiliza el método max() para encontrar el número más grande en la lista "numeros".
    # 3. Utiliza el método remove() para eliminar el número más grande de la lista "numeros".
    # 4. Imprime la lista "numeros" después de eliminar el número más grande.
# En otras palabras, este programa elimina el elemento más grande de la lista y muestra el resultado.
def eliminar_valor_maximo():
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))
    print(numeros)

def mostrar_dos_primeros_10_30():
    lista_10_30 = list(range(10, 31, 5))
    print("6) Dos primeros de 10 a 30 en pasos de 5:", lista_10_30[:2])

def reemplazar_valores_centrales_autos():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1:3] = ["coupe", "convertible"]
    print("7) Lista 'autos' modificada:", autos)

def generar_lista_dobles():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print("8) Lista 'dobles':", dobles)

def actualizar_lista_compras():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][compras[1].index("fideos")] = "tallarines"
    compras[0].remove("pan")
    print("9) Lista 'compras' tras modificaciones:", compras)

def construir_lista_anidada():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print("10) Lista anidada resultante:", lista_anidada)

def main():
    while True:
        print("\n===== MENÚ DE EJERCICIOS DE LISTAS =====")
        print("1) Listar múltiplos de 4 del 1 al 100")
        print("2) Mostrar el penúltimo favorito")
        print("3) Crear y rellenar lista de palabras")
        print("4) Reemplazar elementos en la lista de animales")
        print("5) Eliminar el valor máximo de una lista")
        print("6) Mostrar los dos primeros valores de 10 a 30 en saltos de 5")
        print("7) Reemplazar valores centrales en la lista de autos")
        print("8) Generar lista con el doble de 5, 10 y 15")
        print("9) Actualizar lista de compras")
        print("10) Construir lista anidada")
        print("0) Salir")
        
        opcion = input("\nSeleccione la actividad que desea ejecutar (0–10): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        elif opcion == "1":
            print("\n[EJECUTANDO] Listar múltiplos de 4…")
            listar_multiplos_de_4()
        elif opcion == "2":
            print("\n[EJECUTANDO] Mostrar penúltimo favorito…")
            mostrar_penultimo_elemento_favoritos()
        elif opcion == "3":
            print("\n[EJECUTANDO] Crear y rellenar lista de palabras…")
            crear_y_rellenar_lista_palabras()
        elif opcion == "4":
            print("\n[EJECUTANDO] Reemplazar elementos en lista de animales…")
            reemplazar_animales()
        elif opcion == "5":
            print("\n[EJECUTANDO] Eliminar valor máximo de la lista…")
            eliminar_valor_maximo()
        elif opcion == "6":
            print("\n[EJECUTANDO] Mostrar dos primeros valores de la lista 10–30…")
            mostrar_dos_primeros_10_30()
        elif opcion == "7":
            print("\n[EJECUTANDO] Reemplazar valores centrales en lista de autos…")
            reemplazar_valores_centrales_autos()
        elif opcion == "8":
            print("\n[EJECUTANDO] Generar lista de dobles…")
            generar_lista_dobles()
        elif opcion == "9":
            print("\n[EJECUTANDO] Actualizar lista de compras…")
            actualizar_lista_compras()
        elif opcion == "10":
            print("\n[EJECUTANDO] Construir lista anidada…")
            construir_lista_anidada()
        else:
            print("\n[ERROR] Opción no válida. Por favor ingrese un número entre 0 y 10.")
        
        input("\nPresione Enter para volver al menú…")
        print("\n" + "="*50)

main()