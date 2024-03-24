from typing import List

def factN_rec(x: int, n: int) -> int:
    """
    Función que calcula el factorial de un número x, con saltos de n en n.

    Args:
    x -- Número al que se le calculará el factorial.
    n -- Número de saltos que se darán en cada iteración.

    Returns:
    int -- El factorial de x.
    """
    assert isinstance(x, int) and x >= 0, "x debe ser no negativo"
    assert isinstance(n, int) and n > 0, "n debe ser positivo"

    if x < n:
        return 1
    else:
        return x * factN_rec(x - n, n)

def factN_iter(x: int, n: int) -> int:
    """
    Función que calcula el factorial de un número x, con saltos de n en n.

    Args:
    x -- Número al que se le calculará el factorial.
    n -- Número de saltos que se darán en cada iteración.

    Returns:
    int -- El factorial de x.
    """
    assert isinstance(x, int) and x >= 0, "x debe ser no negativo"
    assert isinstance(n, int) and n > 0, "n debe ser positivo"

    result: int = 1
    while x >= n:
        result *= x
        x -= n
    return result

def fusc_rec(n: int) -> int:
    """
    Función que calcula el n-ésimo número de la sucesión de Fusc.

    Args:
    n -- Número de la sucesión.

    Returns:
    int -- El n-ésimo número de la sucesión.
    """
    assert isinstance(n, int) and n >= 0, "n should be a non-negative integer"

    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    elif n % 2 == 0:
        return fusc_rec(n // 2)
    
    else:
        return fusc_rec(n // 2) + fusc_rec(n // 2 + 1) 
    
def potencia_rec(n: int, m: int) -> int:
    """
    Función que calcula la potencia de un número n elevado a la m.

    Args:
    n -- Número base.
    m -- Número exponente.

    Returns:
    int -- El resultado de la potencia n^m.
    """
    assert isinstance(n, int), "n debe ser un entero"
    assert isinstance(m, int) and m >= 0, "m debe ser un entero no negativo"

    if m == 0:
        return 1
    
    elif m % 2 == 0:
        return potencia_rec(n * n, m // 2)
    
    else:
        return n * potencia_rec(n, m - 1)

def potencia_iter(n: int, m: int) -> int:
    """
    Función que calcula la potencia de un número n elevado a la m.

    Args:
    n -- Número base.
    m -- Número exponente.

    Returns:
    int -- El resultado de la potencia n^m.
    """
    assert isinstance(n, int), "n debe ser un entero"
    assert isinstance(m, int) and m >= 0, "m debe ser un entero no negativo"

    result: int = 1
    while m > 0:
        if m % 2 == 1:
            result *= n
        m //= 2
        n *= n
    
    return result

def mcd_rec(n: int, m: int) -> int:
    """
    Función que calcula el máximo común divisor entre dos números n y m.

    Args:
    n -- Número n.
    m -- Número m.

    Returns:
    int -- El máximo común divisor entre n y m.
    """
    assert isinstance(n, int) and n > 0, "n debe ser un entero positivo"
    assert isinstance(m, int) and m > 0, "m debe ser un entero positivo"

    if n == m:
        return n
    
    elif n > m:
        return mcd_rec(n - m, m)
    
    else:
        return mcd_rec(n, m - n)

def mcd_iter(n: int, m: int) -> int:
    """
    Función que calcula el máximo común divisor entre dos números n y m.

    Args:
    n -- Número n.
    m -- Número m.

    Returns:
    int -- El máximo común divisor entre n y m.
    """
    assert isinstance(n, int) and n > 0, "n debe ser un entero positivo"
    assert isinstance(m, int) and m > 0, "m debe ser un entero positivo"

    while n != m:
        if n > m:
            n -= m
    
        else:
            m -= n
    
    return n

def combinatorio_rec(n: int, k: int) -> int:
    """
    Función que calcula el coeficiente binomial de n sobre k.

    Args:
    n -- Número n.
    k -- Número k.

    Returns:
    int -- El coeficiente binomial de n sobre k.
    """
    assert isinstance(n, int) and n >= 0, "n debe ser no negativo"
    assert isinstance(k, int) and k >= 0, "k debe ser no negativo"

    if k == 0:
        return 1
    
    elif k > n:
        return 0
    
    else:
        return combinatorio_rec(n - 1, k - 1) + combinatorio_rec(n - 1, k)
    
def stirling_rec(n: int, k: int) -> int:
    """
    Función que calcula los números de Stirling de segunda clase.

    Args:
    n -- Número n.
    k -- Número k.

    Returns:
    int -- El número de Stirling de segunda clase.
    """
    assert isinstance(n, int) and n >= 0, "n debe ser no negativo"
    assert isinstance(k, int) and k >= 0, "k debe ser no negativo"
    
    if k == 1 or k == n:
        return 1
    
    elif k > n or (n > 0 and k == 0):
        return 0
    
    elif k == n - 1:
        return combinatorio_rec(n, 2)
    
    elif k == 2 and n > 0:
        return 2**(n-1) - 1
    
    else:
        return stirling_rec(n - 1, k - 1) + k * stirling_rec(n - 1, k)
    
def ackerman_rec(m: int, n: int) -> int:
    """
    Función que calcula la función de Ackerman.

    Args:
    m -- Número m.
    n -- Número n.

    Returns:
    int -- El resultado de la función de Ackerman.
    """
    assert isinstance(m, int) and m >= 0, "m debe ser no negativo"
    assert isinstance(n, int) and n >= 0, "n debe ser no negativo"

    if m == 0:
        return n + 1
    
    elif n == 0:
        return ackerman_rec(m - 1, 1)
    
    else:
        return ackerman_rec(m - 1, ackerman_rec(m, n - 1))
    
def bs_rec(A: List[int], l: int, r: int, x: int) -> int:
    """
    Función que realiza una búsqueda binaria recursiva en una lista de enteros.

    Args:
    A -- Lista de enteros.
    l -- Índice izquierdo.
    r -- Índice derecho.
    x -- Elemento a buscar.

    Returns:
    int -- El índice del elemento buscado.
    """
    assert isinstance(A, list), "A debe ser una lista"
    assert isinstance(l, int) and l >= 0, "l debe ser un entero no negativo"
    assert isinstance(r, int) and r >= 0, "r debe ser un entero no negativo"
    assert isinstance(x, int), "x debe ser un entero"
    
    if l > r:
        return -1
    mid: int = (l + r) // 2

    if A[mid] == x:
        return mid
    
    elif A[mid] > x:
        return bs_rec(A, l, mid - 1, x)
    
    else:
        return bs_rec(A, mid + 1, r, x)