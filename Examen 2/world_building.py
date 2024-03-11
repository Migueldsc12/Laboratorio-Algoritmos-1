# Examen 2 Laboratorio de algoritmos y estructuras 1
# Autor: Miguel Salomon - 1910274

import math
import copy
from typing import List

def crear_mundo()-> List[List[str]]:
    """
    Crea un mundo de dimensiones MxN lleno de Tierra.

    Retorna:
    Una lista de M listas, cada una con N elementos, todos iguales a 'T'.
    """
    while True:
        M: int = int(input("Ingrese el número de filas (M): "))

        if M > 0:
            break
        
        else:
            print("Error: M debe ser mayor a 0. Intente de nuevo.")

    while True:
        N: int = int(input("Ingrese el número de columnas (N): "))
        
        if N > 0:
            break
        
        else:
            print("Error: N debe ser mayor a 0. Intente de nuevo.")

    # Crear un mundo lleno de Tierra
    mundo: List[List[str]] = [['\033[1;32mT\033[0m'] * N for _ in range(M)]

    return mundo

#-------------------------------------------------------------------------------------

def imprimir_mundo(mundo: List[List[str]]) -> None:
    """
    Imprime el mundo en la consola, con cada casilla representada por un caracter.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    for fila in mundo:
        print(" ".join(f"{casilla:5}" for casilla in fila))
    print()
    
#-------------------------------------------------------------------------------------

def agregar_ciudad(mundo: List[List[str]]) -> None:
    """
    Agrega una ciudad al mundo, representada por la letra 'C'.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X: "))
        Y: int = int(input("Ingrese la coordenada Y: "))
        L: int = int(input("Ingrese el lado L: "))

        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and L > 0:
        
            for i in range(X, min(X + L, len(mundo))):
        
                for j in range(Y, min(Y + L, len(mundo[0]))):
                    mundo[i][j] = "\033[1mC\033[0m"
            print("Ciudad agregada exitosamente.")
        
        else:
            print("Coordenadas o tamaño de ciudad no válidos. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")


#-------------------------------------------------------------------------------------
            
def agregar_rio(mundo: List[List[str]]) -> None:
    """
    Agrega un río al mundo, representado por la letra 'A'.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X del punto central del río: "))
        Y: int = int(input("Ingrese la coordenada Y del punto central del río: "))
        
        print("Seleccione la dirección del río:")
        print("1. Vertical")
        print("2. Horizontal")
        print("3. Diagonal")
        print("4. Diagonal inversa")
        
        direccion: int = int(input("Ingrese el número correspondiente a la dirección del río: "))
        
        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and 1 <= direccion <= 4:
        
            for i in range(len(mundo)):
        
                for j in range(len(mundo[0])):
        
                    if direccion == 1 and j >= Y - 1 and j <= Y + 1:
                        mundo[i][j] = "\033[1;36mA\033[0m"
        
                    elif direccion == 2 and i >= X - 1 and i <= X + 1:
                        mundo[i][j] = "\033[1;36mA\033[0m"
        
                    elif direccion == 3 and i - X >= j - Y - 1 and i - X <= j - Y + 1:
                        mundo[i][j] = "\033[1;36mA\033[0m"
        
                    elif direccion == 4 and i - X >= Y - j - 1 and i - X <= Y - j + 1:
                        mundo[i][j] = "\033[1;36mA\033[0m"
            print("Río agregado exitosamente.")
        
        else:
            print("Coordenadas o dirección del río no válidos. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")

#-------------------------------------------------------------------------------------

def agregar_montana(mundo: List[List[str]]) -> None:
    """
    Agrega una montaña al mundo, representada por la letra 'M'.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X del centro de la montaña: "))
        Y: int = int(input("Ingrese la coordenada Y del centro de la montaña: "))
        R: int = int(input("Ingrese el radio de la montaña: "))
        
        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and R > 0:
        
            for i in range(len(mundo)):
        
                for j in range(len(mundo[0])):
                    distancia = math.sqrt((i - X)**2 + (j - Y)**2)
        
                    if distancia <= R:
                        mundo[i][j] = "\033[1;31mM\033[0m"
            
            print("Montaña agregada exitosamente.")
        
        else:
            print("Coordenadas o radio de la montaña no válidos. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")

#-------------------------------------------------------------------------------------
        
def aplanar(mundo: List[List[str]]) -> None:
    """
    Aplana una forma específica en el mundo.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    print("Seleccione la forma a aplanar:")
    print("1. Ciudad")
    print("2. Río")
    print("3. Montaña")

    try:
        opcion: int = int(input("Ingrese el número de la forma: "))
        
        if opcion == 1:
            aplanar_ciudad(mundo)
        
        elif opcion == 2:
            aplanar_rio(mundo)
        
        elif opcion == 3:
            aplanar_montana(mundo)
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese un número.")

def aplanar_ciudad(mundo: List[List[str]]) -> None:
    """
    aplana el mundo en forma de ciudad.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X de la ciudad: "))
        Y: int = int(input("Ingrese la coordenada Y de la ciudad: "))
        L: int = int(input("Ingrese el lado de la ciudad: "))
        
        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and L > 0:
        
            for i in range(X, min(X + L, len(mundo))):
        
                for j in range(Y, min(Y + L, len(mundo[0]))):
                    mundo[i][j] = "\033[1;32mT\033[0m"
            print("Ciudad aplanada exitosamente.")
        
        else:
            print("Coordenadas o lado de la ciudad no válidos. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")

def aplanar_rio(mundo: List[List[str]]) -> None:
    """
    aplana el mundo en forma de río.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """

    try:
        X: int = int(input("Ingrese la coordenada X del punto inicial del río: "))
        Y: int = int(input("Ingrese la coordenada Y del punto inicial del río: "))
        
        print("Seleccione la dirección del río:")
        print("1. Vertical")
        print("2. Horizontal")
        print("3. Diagonal")
        print("4. Diagonal inversa")
        
        direccion: int = int(input("Ingrese el número correspondiente a la dirección del río: "))
        
        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and 1 <= direccion <= 4:
            
            for i in range(len(mundo)):
            
                for j in range(len(mundo[0])):
            
                    if direccion == 1 and j >= Y - 1 and j <= Y + 1:
                        mundo[i][j] = "\033[1;32mT\033[0m"
            
                    elif direccion == 2 and i >= X - 1 and i <= X + 1:
                        mundo[i][j] = "\033[1;32mT\033[0m"
            
                    elif direccion == 3 and i - X >= j - Y - 1 and i - X <= j - Y + 1:
                        mundo[i][j] = "\033[1;32mT\033[0m"
            
                    elif direccion == 4 and i - X >= Y - j - 1 and i - X <= Y - j + 1:
                        mundo[i][j] = "\033[1;32mT\033[0m"
            
            else:
                print("Dirección no válida. Inténtelo de nuevo.")
                return
            
        print("Río aplanado exitosamente.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")



def aplanar_montana(mundo: List[List[str]]) -> None:
    """
    aplana el mundo en forma de montaña.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X del centro de la montaña: "))
        Y: int = int(input("Ingrese la coordenada Y del centro de la montaña: "))
        R: int = int(input("Ingrese el radio de la montaña: "))
        
        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and R > 0:
            
            for i in range(len(mundo)):
            
                for j in range(len(mundo[0])):
                    distancia = math.sqrt((i - X)**2 + (j - Y)**2)
            
                    if distancia <= R:
                        mundo[i][j] = "\033[1;32mT\033[0m"
            print("Montaña aplanada exitosamente.")
        
        else:
            print("Coordenadas o radio de la montaña no válidos. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")


#-------------------------------------------------------------------------------------

def eliminar_zona(mundo: List[List[str]]) -> None:
    """
    Elimina una forma específica en el mundo.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        forma: int = int(input("Seleccione la forma de la zona a eliminar:\n1. Ciudad\n2. Río\n3. Montaña\n"))
        
        if forma == 1:  # Ciudad
            eliminar_ciudad(mundo)
        
        elif forma == 2:  # Río
            eliminar_rio(mundo)
        
        elif forma == 3:  # Montaña
            eliminar_montana(mundo)
        
        else:
            print("Forma no válida. Inténtelo de nuevo.")
    
    except ValueError:
        print("Por favor, ingrese un valor numérico.")

# Funciones auxiliares para eliminar cada forma específica

def eliminar_ciudad(mundo: List[List[str]]) -> None:
    """
    elimina una zona en forma de ciudad.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X del punto inicial de la ciudad: "))
        Y: int = int(input("Ingrese la coordenada Y del punto inicial de la ciudad: "))
        L: int = int(input("Ingrese el tamaño de la ciudad (lado del cuadrado): "))
        
        for i in range(X, X + L):
        
            for j in range(Y, Y + L):
        
                if 0 <= i < len(mundo) and 0 <= j < len(mundo[0]):
                    mundo[i][j] = "\033[40m \033[0m"
        
        print("Ciudad eliminada exitosamente.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")

def eliminar_rio(mundo: List[List[str]]) -> None:
    """
    elimina una zona en forma de río.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X = int(input("Ingrese la coordenada X del punto inicial del río: "))
        Y = int(input("Ingrese la coordenada Y del punto inicial del río: "))

        direccion = int(input("Seleccione la dirección del río:\n1. Vertical\n2. Horizontal\n3. Diagonal\n4. Diagonal inversa\n"))

        if 0 <= X < len(mundo) and 0 <= Y < len(mundo[0]) and 1 <= direccion <= 4:
        
            for i in range(len(mundo)):
        
                for j in range(len(mundo[0])):
        
                    if direccion == 1 and j >= Y - 1 and j <= Y + 1:
                        mundo[i][j] = "\033[40m \033[0m"
        
                    elif direccion == 2 and i >= X - 1 and i <= X + 1:
                        mundo[i][j] = "\033[40m \033[0m"
        
                    elif direccion == 3 and i - X >= j - Y - 1 and i - X <= j - Y + 1:
                        mundo[i][j] = "\033[40m \033[0m"
        
                    elif direccion == 4 and i - X >= Y - j - 1 and i - X <= Y - j + 1:
                        mundo[i][j] = "\033[40m \033[0m"
        
            print("Río eliminado exitosamente.")
        
        else:
            print("Dirección no válida. Inténtelo de nuevo.")

    except ValueError:
        print("Por favor, ingrese valores numéricos.")


def eliminar_montana(mundo: List[List[str]]) -> None:
    """
    elimina una zona en forma de montaña.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        X: int = int(input("Ingrese la coordenada X del centro de la montaña: "))
        Y: int = int(input("Ingrese la coordenada Y del centro de la montaña: "))
        R: int = int(input("Ingrese el radio de la montaña: "))
        
        for i in range(len(mundo)):
        
            for j in range(len(mundo[0])):
                distancia = ((i - X) ** 2 + (j - Y) ** 2) ** 0.5
        
                if distancia <= R:
                    mundo[i][j] = "\033[40m \033[0m"
        
        print("Montaña eliminada exitosamente.")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos.")


#-------------------------------------------------------------------------------------
        
def redimensionar(mundo: List[List[str]]) -> None:
    """
    Redimensiona el mundo a una nueva dimensión MxN.

    Args:
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """
    try:
        M: int = int(input("Ingrese la nueva dimensión M: "))
        N: int = int(input("Ingrese la nueva dimensión N: "))
        
        if M <= 0 or N <= 0:
            print("Error: Ingrese dimensiones válidas (M y N deben ser mayores a 0).")
            return

        viejas_filas: int = len(mundo)
        viejas_columnas: int = len(mundo[0])

        nuevos_filas: int = min(M, viejas_filas)
        nuevos_columnas: int = min(N, viejas_columnas)

        nuevo_mundo: List[List[str]] = [["\033[1;32mT\033[0m"] * N for _ in range(M)]

        for i in range(nuevos_filas):
        
            for j in range(nuevos_columnas):
                nuevo_mundo[i][j] = mundo[i][j]

        mundo.clear()
        mundo.extend(nuevo_mundo)

        print("Redimensión exitosa.")
    
    except ValueError:
        print("Error: Ingrese números enteros positivos para M y N.")

#-------------------------------------------------------------------------------------
        
def deshacer(undo_stack: List[str], mundo: List[List[str]]) -> None:
    """
    Deshace la última acción realizada en el mundo.

    Args:
    undo_stack: Una lista que contiene las acciones realizadas en el mundo.
    mundo: Una lista de M listas, cada una con N elementos, todos iguales a 'T'.

    Returns:
    None
    """

    if undo_stack:
        accion, estado_anterior = undo_stack.pop()

        if accion == "redimensionar":
            print("No se puede deshacer la redimensión.")

        else:
            mundo.clear()
            mundo.extend(estado_anterior)
            print(f"Deshaciendo última acción: {accion}")

    else:
        print("No hay acciones para deshacer.")

#-------------------------------------------------------------------------------------

def menu_principal() -> None:
    """
    Muestra el menú principal y permite al usuario realizar acciones en el mundo.

    Returns:
    None
    """

    mundo: List[List[str]] = crear_mundo()
    undo_stack: List[str] = []

    while True:

        print("\nMENU PRINCIPAL:")
        print("1. Imprimir mundo.")
        print("2. Agregar ciudad.")
        print("3. Agregar río.")
        print("4. Agregar montaña.")
        print("5. Aplanar.")
        print("6. Eliminar zona.")
        print("7. Redimensionar.")
        print("8. Deshacer.")
        print("9. Salir.")

        opcion: str = input("Seleccione una opción: ")

        if opcion == "1":
            imprimir_mundo(mundo)
        
        elif opcion == "2":
            undo_stack.append(("agregar ciudad", copy.deepcopy(mundo)))
            agregar_ciudad(mundo)
        
        elif opcion == "3":
            undo_stack.append(("agregar río", copy.deepcopy(mundo)))
            agregar_rio(mundo)
        
        elif opcion == "4":
            undo_stack.append(("agregar montaña", copy.deepcopy(mundo)))
            agregar_montana(mundo)
        
        elif opcion == "5":
            undo_stack.append(("aplanar", copy.deepcopy(mundo)))
            aplanar(mundo)
        
        elif opcion == "6":
            undo_stack.append(("eliminar zona", copy.deepcopy(mundo)))
            eliminar_zona(mundo)
        
        elif opcion == "7":
            undo_stack.append(("redimensionar", copy.deepcopy(mundo)))
            redimensionar(mundo)
        
        elif opcion == "8":
            deshacer(undo_stack, mundo)
        
        elif opcion == "9":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

menu_principal()
