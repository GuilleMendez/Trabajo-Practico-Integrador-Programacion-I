import csv
import os

ARCHIVO = "paises.csv"


# ==========================
# CARGA Y GUARDADO
# ==========================

def cargar_datos():
    paises = []

    if not os.path.exists(ARCHIVO):
        return paises

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })

    except Exception:
        print("Error: formato incorrecto del archivo CSV.")

    return paises


def guardar_datos(paises):
    try:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(paises)

        print("Datos guardados correctamente.")

    except Exception as e:
        print("Error al guardar:", e)


# ==========================
# AGREGAR
# ==========================

def agregar_pais(paises):

    # Nombre
    while True:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        # Validar duplicado
        existe = False
        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print("Ese país ya existe.")
            continue

        break  # nombre válido

    # Continente
    while True:
        continente = input("Continente: ").strip()
        if continente == "":
            print("El continente no puede estar vacío.")
        else:
            break

    # Población
    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion < 0:
                print("La población debe ser positiva.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Superficie
    while True:
        try:
            superficie = int(input("Superficie (km²): "))
            if superficie < 0:
                print("La superficie debe ser positiva.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Agregar país
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    print("País agregado correctamente.")


# ==========================
# ACTUALIZAR
# ==========================

def actualizar_pais(paises):

    # Buscar país
    while True:
        nombre = input("Ingrese el país a actualizar: ").strip()

        # Buscar coincidencia
        pais_encontrado = None
        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                pais_encontrado = pais
                break

        if pais_encontrado is None:
            print("País no encontrado. Intente nuevamente.")
            continue
        else:
            break  # país encontrado

    # Actualizar población
    while True:
        try:
            nueva_poblacion = int(input("Nueva población: "))
            if nueva_poblacion < 0:
                print("La población debe ser positiva.")
                continue
            pais_encontrado["poblacion"] = nueva_poblacion
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Actualizar superficie
    while True:
        try:
            nueva_superficie = int(input("Nueva superficie: "))
            if nueva_superficie < 0:
                print("La superficie debe ser positiva.")
                continue
            pais_encontrado["superficie"] = nueva_superficie
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    print("Datos actualizados.")



# ==========================
# BUSCAR
# ==========================

def buscar_pais(paises):

    while True:
        texto = input("Buscar país: ").strip().lower()

        if texto == "":
            print("Debe ingresar un texto para buscar.")
            continue

        resultados = []

        for pais in paises:
            if texto in pais["nombre"].lower():
                resultados.append(pais)

        if len(resultados) == 0:
            print("No se encontraron resultados. Intente nuevamente.")
            continue  # vuelve a pedir el input

        # Si encontró resultados, los muestra y sale del while
        mostrar_lista(resultados)
        break


# ==========================
# FILTROS
# ==========================

def filtrar_continente(paises):

    while True:
        continente = input("Continente: ").strip().lower()

        if continente == "":
            print("Debe ingresar un continente.")
            continue

        resultados = [
            p for p in paises
            if p["continente"].lower() == continente
        ]

        if not resultados:
            print("Sin resultados. Intente nuevamente.")
            continue

        mostrar_lista(resultados)
        break


def filtrar_poblacion(paises):

   def filtrar_poblacion(paises):

    while True:
        try:
            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))

            if minimo > maximo:
                print("Rango inválido. El mínimo no puede ser mayor que el máximo.")
                continue  # vuelve a pedir

            resultados = [
                p for p in paises
                if minimo <= p["poblacion"] <= maximo
            ]

            if not resultados:
                print("Sin resultados.")
                break  # <<--- como pediste: sale del while

            mostrar_lista(resultados)
            break  # sale del while si todo está bien

        except ValueError:
            print("Debe ingresar números enteros. Intente nuevamente.")


def filtrar_superficie(paises):

    while True:
        try:
            minimo = int(input("Superficie mínima: "))
            maximo = int(input("Superficie máxima: "))

            if minimo > maximo:
                print("Rango inválido. El mínimo no puede ser mayor que el máximo.")
                continue  # vuelve a pedir

            resultados = [
                p for p in paises
                if minimo <= p["superficie"] <= maximo
            ]

            if not resultados:
                print("Sin resultados.")
                break  # <<--- como pediste: sale del while

            mostrar_lista(resultados)
            break  # sale del while si todo está bien

        except ValueError:
            print("Debe ingresar números enteros. Intente nuevamente.")


# ==========================
# ORDENAMIENTOS
# ==========================

def ordenar_nombre(paises):

    orden = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    reverse = orden == "D"

    ordenados = sorted(
        paises,
        key=lambda x: x["nombre"].lower(),
        reverse=reverse
    )

    mostrar_lista(ordenados)


def ordenar_poblacion(paises):

    orden = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    reverse = orden == "D"

    ordenados = sorted(
        paises,
        key=lambda x: x["poblacion"],
        reverse=reverse
    )

    mostrar_lista(ordenados)


def ordenar_superficie(paises):

    orden = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    reverse = orden == "D"

    ordenados = sorted(
        paises,
        key=lambda x: x["superficie"],
        reverse=reverse
    )

    mostrar_lista(ordenados)


# ==========================
# ESTADISTICAS
# ==========================

def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos.")
        return

    mayor = max(
        paises,
        key=lambda x: x["poblacion"]
    )

    menor = min(
        paises,
        key=lambda x: x["poblacion"]
    )

    promedio_poblacion = (
        sum(p["poblacion"] for p in paises)
        / len(paises)
    )

    promedio_superficie = (
        sum(p["superficie"] for p in paises)
        / len(paises)
    )

    continentes = {}

    for pais in paises:

        cont = pais["continente"]

        if cont not in continentes:
            continentes[cont] = 0

        continentes[cont] += 1

    print("\n===== ESTADÍSTICAS =====")

    print(
        f"Mayor población: {mayor['nombre']} "
        f"({mayor['poblacion']})"
    )

    print(
        f"Menor población: {menor['nombre']} "
        f"({menor['poblacion']})"
    )

    print(
        f"Promedio población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nPaíses por continente:")

    for cont, cantidad in continentes.items():
        print(f"{cont}: {cantidad}")


# ==========================
# UTILIDADES
# ==========================

def mostrar_lista(lista):

    print("\n----------------------------")

    for pais in lista:

        print(
            f"{pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} km² | "
            f"{pais['continente']}"
        )

    print("----------------------------")


# ==========================
# MENU
# ==========================

def menu():

    paises = cargar_datos()

    while True:

        print("\n===== SISTEMA DE PAÍSES =====")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar por nombre")
        print("8. Ordenar por población")
        print("9. Ordenar por superficie")
        print("10. Mostrar estadísticas")
        print("11. Guardar cambios")
        print("0. Salir")

        opcion = input("\nOpción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_continente(paises)

        elif opcion == "5":
            filtrar_poblacion(paises)

        elif opcion == "6":
            filtrar_superficie(paises)

        elif opcion == "7":
            ordenar_nombre(paises)

        elif opcion == "8":
            ordenar_poblacion(paises)

        elif opcion == "9":
            ordenar_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "11":
            guardar_datos(paises)

        elif opcion == "0":

            guardar = input(
                "¿Guardar antes de salir? (S/N): "
            ).upper()

            if guardar == "S":
                guardar_datos(paises)

            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

menu()