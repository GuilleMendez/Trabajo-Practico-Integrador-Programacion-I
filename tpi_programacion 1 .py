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

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    continente = input("Continente: ").strip()

    if continente == "":
        print("El continente no puede estar vacío.")
        return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie (km²): "))

        if poblacion < 0 or superficie < 0:
            print("Los valores deben ser positivos.")
            return

    except ValueError:
        print("Debe ingresar números enteros.")
        return

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

    nombre = input("Ingrese el país a actualizar: ").strip()

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            try:
                pais["poblacion"] = int(
                    input("Nueva población: ")
                )

                pais["superficie"] = int(
                    input("Nueva superficie: ")
                )

                print("Datos actualizados.")
                return

            except ValueError:
                print("Valores inválidos.")
                return

    print("País no encontrado.")


# ==========================
# BUSCAR
# ==========================

def buscar_pais(paises):

    texto = input("Buscar país: ").lower()

    resultados = []

    for pais in paises:
        if texto in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron resultados.")
        return

    mostrar_lista(resultados)


# ==========================
# FILTROS
# ==========================

def filtrar_continente(paises):

    continente = input("Continente: ").lower()

    resultados = [
        p for p in paises
        if p["continente"].lower() == continente
    ]

    if not resultados:
        print("Sin resultados.")
        return

    mostrar_lista(resultados)


def filtrar_poblacion(paises):

    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))

        if minimo > maximo:
            print("Rango inválido.")
            return

        resultados = [
            p for p in paises
            if minimo <= p["poblacion"] <= maximo
        ]

        if not resultados:
            print("Sin resultados.")
            return

        mostrar_lista(resultados)

    except ValueError:
        print("Debe ingresar números.")


def filtrar_superficie(paises):

    try:
        minimo = int(input("Superficie mínima: "))
        maximo = int(input("Superficie máxima: "))

        if minimo > maximo:
            print("Rango inválido.")
            return

        resultados = [
            p for p in paises
            if minimo <= p["superficie"] <= maximo
        ]

        if not resultados:
            print("Sin resultados.")
            return

        mostrar_lista(resultados)

    except ValueError:
        print("Debe ingresar números.")


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