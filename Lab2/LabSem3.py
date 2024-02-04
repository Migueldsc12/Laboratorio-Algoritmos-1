from typing import List

def es_primo(num: int) -> bool:
    """
    Verifica si un número entero positivo es primo.
    
    Parametros:
    - num (int): Número entero positivo a verificar.
    
    Returno:
    - bool: True si el número es primo, False de lo contrario.
    """
    if num < 2:
        return False

    i: int = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

def suma_cuadrado_impares(num: int) -> int:
    """
    Calcula la suma del cuadrado de todos los números impares en el intervalo [0, num).
    
    Parametros:
    - num (int): Número entero positivo.
    
    Retorno:
    - int: Suma de los cuadrados de los números impares.
    """
    suma: int = 0
    i: int = 1
    while i < num:
        suma += i**2
        i += 2
    return suma

def son_amigos(m: int, n: int) -> bool:
    """
    Verifica si dos números enteros positivos son amigos.
    
    Parametros:
    - m (int): Primer número entero positivo.
    - n (int): Segundo número entero positivo.
    
    Retorno:
    - bool: True si los números son amigos, False de lo contrario.
    """
    # Suma de los divisores propios de m
    suma_m: int = 1  
    i_m: int = 2
    while i_m**2 <= m:
        if m % i_m == 0:
            suma_m += i_m
            if i_m != m // i_m:
                suma_m += m // i_m
        i_m += 1

    # Suma de los divisores propios de n
    suma_n: int = 1
    i_n: int = 2
    while i_n**2 <= n:
        if n % i_n == 0:
            suma_n += i_n
            if i_n != n // i_n:
                suma_n += n // i_n
        i_n += 1

    return suma_m == n and suma_n == m

def esta_ordenado(numeros: List[float]) -> bool:
    """
    Verifica si una lista de números reales está ordenada en orden no decreciente.
    
    Parameters:
    - numeros (List[float]): Lista de números reales.
    
    Returns:
    - bool: True si la lista está ordenada en orden no decreciente, False de lo contrario.
    """
    i: float = 0
    while i < len(numeros) - 1:
        if numeros[i] > numeros[i + 1]:
            return False
        i += 1
    return True


def buscar(numeros: List[float], n: float) -> int:
    """
    Busca la primera instancia de un número real en una lista y devuelve su posición.
    Si el número no está en la lista, devuelve -1.
    
    Parameters:
    - numeros (List[float]): Lista de números reales.
    - n (float): Número real a buscar en la lista.
    
    Returns:
    - int: Posición del primer elemento igual a n, o -1 si no se encuentra.
    """
    i: int = 0
    while i < len(numeros):
        if numeros[i] == n:
            return i
        i += 1
    return -1

def promedio(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista no vacía de números reales.
    
    Parametros:
    - numeros (List[float]): Lista de números reales.
    
    Retorno:
    - float: Promedio de los números en la lista.
    """
    suma_total: float = 0
    i: int = 0

    while i < len(numeros):
        suma_total += numeros[i]
        i += 1

    cantidad_elementos:float = len(numeros)
    
    return suma_total / cantidad_elementos
    
def suma_maximo(matriz: List[List[int]]) -> int:
    """
    Encuentra el valor de la suma del máximo de cada fila en una matriz de números enteros.
    
    Parametros:
    - matriz (List[List[int]]): Matriz de números enteros.
    
    Retorno:
    - int: Suma de los máximos de cada fila.
    """
    suma: int = 0

    for fila in matriz:
        if fila:
            maximo_fila: int = fila[0] 
            for elemento in fila:
                if elemento > maximo_fila:
                    maximo_fila: int = elemento
            suma += maximo_fila

    return suma

def es_simetrica(matriz: List[List[int]]) -> bool:
    """
    Determina si una matriz N x N de números enteros es simétrica.
    
    Parametros:
    - matriz (List[List[int]]): Matriz de números enteros.
    
    Retorno:
    - bool: True si la matriz es simétrica, False de lo contrario.
    """
    n: int = len(matriz)

    i: int = 0
    while i < n:
        j: int = i + 1
        while j < n:
            if matriz[i][j] != matriz[j][i]:
                return False
            j += 1
        i += 1

    return True

def es_palindromo(palabra: str) -> bool:
    """
    Verifica si una palabra es un palíndromo.
    
    Parametros:
    - palabra (str): Palabra a verificar.
    
    Retorno:
    - bool: True si la palabra es un palíndromo, False de lo contrario.
    """
    longitud: int = len(palabra)
    i: int = 0
    j: int = longitud - 1

    while i < j:
        if palabra[i] != palabra[j]:
            return False
        i += 1
        j -= 1

    return True