from typing import Set, List

def es_conjunto(conjunto: Set[int]) -> bool:
    """
    Verifica que una lista cumple con la definición de conjunto.

    Parámetros:
    - conjunto (list): Lista que se verifica como conjunto.

    Retorna:
    - bool: True si es un conjunto, False de lo contrario.
    """
    elementos_vistos: List[int] = []

    for elemento in conjunto:
        if elemento in elementos_vistos:
            return False
        elementos_vistos.append(elemento)

    return True

def union(conjunto1: Set[int], conjunto2: Set[int], en_linea: bool =False) -> Set[int]:
    """
    Representa la unión entre conjuntos.

    Parámetros:
    - conjunto1 (list): Primer conjunto.
    - conjunto2 (list): Segundo conjunto.
    - en_linea (bool): Indica si la operación se realiza en línea.

    Retorna:
    - list: Resultado de la unión.
    """
    assert es_conjunto(conjunto1) and es_conjunto(conjunto2), "Al menos uno de los argumentos no es un conjunto."

    resultado: Set[int] = conjunto1.copy() if not en_linea else conjunto1

    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado

def interseccion(conjunto1: Set[int], conjunto2: Set[int], en_linea: bool = False) -> Set[int]:
    """
    Representa la intersección entre conjuntos.

    Parámetros:
    - conjunto1 (list): Primer conjunto.
    - conjunto2 (list): Segundo conjunto.
    - en_linea (bool): Indica si la operación se realiza en línea.

    Retorna:
    - list: Resultado de la intersección.
    """
    assert es_conjunto(conjunto1) and es_conjunto(conjunto2), "Al menos uno de los argumentos no es un conjunto."

    resultado: Set[int] = [elemento for elemento in conjunto1 if elemento in conjunto2]

    if en_linea:
        conjunto1.clear()
        conjunto1.extend(resultado)

    return resultado

def diferencia(conjunto1: Set[int], conjunto2: Set[int], en_linea: bool = False) -> Set[int]:
    """
    Representa la diferencia entre conjuntos.

    Parámetros:
    - conjunto1 (list): Primer conjunto.
    - conjunto2 (list): Segundo conjunto.
    - en_linea (bool): Indica si la operación se realiza en línea.

    Retorna:
    - list: Resultado de la diferencia.
    """
    assert es_conjunto(conjunto1) and es_conjunto(conjunto2), "Al menos uno de los argumentos no es un conjunto."

    resultado: Set[int] = [elemento for elemento in conjunto1 if elemento not in conjunto2]

    if en_linea:
        conjunto1.clear()
        conjunto1.extend(resultado)

    return resultado

def producto(conjunto1: Set[int], conjunto2: Set[int], en_linea: bool = False) -> Set[int]:
    """
    Devuelve un nuevo conjunto que contiene todos los valores c = a * b
    donde a pertenece a conjunto1 y b pertenece a conjunto2.

    Parámetros:
    - conjunto1 (list): Primer conjunto.
    - conjunto2 (list): Segundo conjunto.
    - en_linea (bool): Indica si la operación se realiza en línea.

    Retorna:
    - list: Resultado del producto.
    """
    assert es_conjunto(conjunto1) and es_conjunto(conjunto2), "Al menos uno de los argumentos no es un conjunto."

    resultado: Set[int] = []

    for a in conjunto1:
        for b in conjunto2:
            producto = a * b
            if producto not in resultado:
                resultado.append(producto)

    if en_linea:
        conjunto1.clear()
        conjunto1.extend(resultado)

    return resultado

def conjunto_de_sumas(conjunto: Set[int], en_linea: bool = False) -> Set[int]:
    """
    Devuelve un nuevo conjunto que contiene la sumatoria de cada subconjunto de A.

    Parámetros:
    - conjunto (list): Conjunto original.
    - en_linea (bool): Indica si la operación se realiza en línea.

    Retorna:
    - list: Resultado del conjunto de sumas.
    """
    assert es_conjunto(conjunto), "El argumento no es un conjunto."

    def obtener_subconjuntos(conjunto: Set[int]) -> Set[Set[int]]:
        """
        Genera todos los subconjuntos de un conjunto dado.

        Parámetros:
        - conjunto (list): Conjunto original.

        Retorna:
        - list: Lista de subconjuntos.
        """
        n: int = len(conjunto)
        subconjuntos: Set[int] = []

        for i in range(2 ** n):
            subconjunto = [conjunto[j] for j in range(n) if (i >> j) & 1]
            subconjuntos.append(subconjunto)

        return subconjuntos

    resultado: Set[int] = [sum(subconjunto) for subconjunto in obtener_subconjuntos(conjunto)]

    if en_linea:
        conjunto.clear()
        conjunto.extend(resultado)

    return resultado

def producto_matricial(matriz1: List[List[int]], matriz2: List[List[int]]) -> List[List[int]]:
    """
    Realiza la multiplicación de dos matrices.

    Parámetros:
    - matriz1 (list): Primera matriz.
    - matriz2 (list): Segunda matriz.

    Retorna:
    - list: Resultado de la multiplicación.
    """
    assert len(matriz1) > 0 and len(matriz2) > 0, "Las matrices no pueden ser vacías."
    assert len(matriz1[0]) == len(matriz2), "Las matrices no son multiplicables."

    n: int = len(matriz1)
    m: int = len(matriz2[0])
    resultado: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def particion(a: List[int], X: int) -> int:
    """
    Realiza la partición de una lista de enteros según el número X.

    Parámetros:
    - a (list): Lista original.
    - X (int): Número entero.

    Retorna:
    - int: Valor de k.
    """
    N: int = len(a)
    k: int = 0

    for i in range(N):
        if a[i] <= X:
            # Mover el elemento a la posición correcta
            temp: int = a.pop(i)
            a.insert(k, temp)
            k += 1

    return k
