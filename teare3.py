import time


PLATOS = {
    "Entradas": {
        "Paella": 200,
        "Gazpacho": 150,
        "Pasta": 300,
        "Ensalada César": 180,
        "Sopa de Verduras": 120
    },
    "Platos Principales": {
        "Filete de Cerdo": 400,
        "Pollo Asado": 280,
        "Bistec a lo Pobre": 500,
        "Trucha": 160,
        "Bacalao": 300,
        "Salmón a la Plancha": 350,
        "Lasaña": 450
    },
    "Postres": {
        "Flan": 200,
        "Naranja": 50,
        "Nueces": 500,
        "Yogur": 100,
        "Helado": 250
    }
}


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time:.4f} segundos")
        return result
    return wrapper


@medir_tiempo
def calcular_calorias_menu():
    """
    Permite al usuario seleccionar una entrada, un plato principal y un postre,
    y calcula el total de calorías del menú elegido.
    """
    print("\n--- CÁLCULO DE CALORÍAS POR MENÚ ---")

    menu_seleccionado = {}
    for categoria, platos_disponibles in PLATOS.items():
        print(f"\nSeleccione un/a {categoria.lower()}:")
        for i, (nombre, calorias) in enumerate(platos_disponibles.items()):
            print(f"{i + 1}. {nombre} ({calorias} cal)")

        while True:
            try:
                opcion = int(input(f"Ingrese el número de su {categoria.lower()} deseado: "))
                if 1 <= opcion <= len(platos_disponibles):
                    nombre_plato = list(platos_disponibles.keys())[opcion - 1]
                    menu_seleccionado[categoria] = (nombre_plato, platos_disponibles[nombre_plato])
                    break
                else:
                    print("Opción inválida. Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

    calorias_por_plato = list(map(lambda item: item[1][1], menu_seleccionado.items()))
    total_calorias = sum(calorias_por_plato)

    print("\n--- MENÚ SELECCIONADO ---")
    for categoria, (nombre, calorias) in menu_seleccionado.items():
        print(f"{categoria}: {nombre} ({calorias} cal)")
    print(f"TOTAL DE CALORÍAS: {total_calorias} cal")

@medir_tiempo
def mostrar_combinaciones_bajas_calorias():
    """
    Muestra todas las combinaciones posibles de entrada + plato principal + postre
    que no superen un límite de calorías indicado por el usuario.
    """
    print("\n--- MENÚS BAJOS EN CALORÍAS ---")
    while True:
        try:
            limite_calorias = int(input("Ingrese el máximo de calorías deseado: "))
            if limite_calorias > 0:
                break
            else:
                print("El límite de calorías debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    entradas = list(PLATOS["Entradas"].items())
    principales = list(PLATOS["Platos Principales"].items())
    postres = list(PLATOS["Postres"].items())

    todas_las_combinaciones = [
        (entrada, principal, postre)
        for entrada in entradas
        for principal in principales
        for postre in postres
    ]

    combinaciones_validas = list(filter(
        lambda combo: sum(item[1] for item in combo) <= limite_calorias,
        todas_las_combinaciones
    ))

    if combinaciones_validas:
        print(f"\nCombinaciones disponibles con menos de {limite_calorias} calorías:")
        for combo in combinaciones_validas:
            total_calorias_combo = sum(item[1] for item in combo)
            print(f"* Entrada: {combo[0][0]} ({combo[0][1]} cal) "
                  f"Principal: {combo[1][0]} ({combo[1][1]} cal) "
                  f"Postre: {combo[2][0]} ({combo[2][1]} cal) "
                  f"TOTAL: {total_calorias_combo} calorías")
    else:
        print(f"No se encontraron combinaciones que no superen las {limite_calorias} calorías.")

    print("\nFin de las combinaciones disponibles.")

def mostrar_menu_principal():
    """
    Muestra el menú principal interactivo al usuario.
    """
    print("\nBIENVENIDO AL SISTEMA DE GESTIÓN DE CALORÍAS DE \"MI MEJOR COMIDA\"")
    print("------------------------------------------------------------------")
    print("1. Calcular calorías de un menú específico")
    print("2. Mostrar combinaciones bajas en calorías")
    print("3. Salir")

def main():
    """
    Función principal que ejecuta el programa.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            calcular_calorias_menu()
        elif opcion == '2':
            mostrar_combinaciones_bajas_calorias()
        elif opcion == '3':
            print("Gracias por usar el Sistema de Gestión de Calorías. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
