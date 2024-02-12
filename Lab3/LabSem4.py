from typing import List

def es_subcadena(s: str, A: str) -> int:
    """
    Obtiene la posición de la primera instancia de s en A.
    Si s no es una subcadena de A, retorna -1.

    Parametros:
    - s (str): Cadena de caracteres a buscar.
    - A (str): Cadena de caracteres en la que buscar.

    Retorno:
    - int: Posición de la primera instancia de s en A, o -1 si no se encuentra.
    """
    i: int = 0
    while i <= len(A) - len(s):
        if A[i:i+len(s)] == s:
            return i
        i += 1

    return -1

def contar_ocurrencias(s1: str, s2: str) -> int:
    """
    Cuenta cuántas veces aparece la primera cadena en la segunda.
    
    Parametros:
    - s1 (str): Primera cadena de caracteres.
    - s2 (str): Segunda cadena de caracteres.
    
    Retorno:
    - int: Número de veces que aparece s1 en s2.
    """
    count: int = 0
    i: int = 0

    while i <= len(s2) - len(s1):
        if s2[i:i+len(s1)] == s1:
            count += 1
            i += len(s1)
        else:
            i += 1

    return count

def comparar_fechas(fecha1: str, fecha2: str) -> bool:
    """
    Compara dos fechas en formato "DD-MM-YYYY" y determina si la primera es mayor que la segunda.
    
    Parametros:
    - fecha1 (str): Primera fecha en formato "DD-MM-YYYY".
    - fecha2 (str): Segunda fecha en formato "DD-MM-YYYY".
    
    Retorno:
    - bool: True si la primera fecha es mayor que la segunda, False de lo contrario.
    """
    # Extraer componentes de las fechas
    dia1, mes1, anio1 = [int(x) for x in fecha1.split('-')]
    dia2, mes2, anio2 = [int(x) for x in fecha2.split('-')]

    # Comparar años
    if anio1 > anio2:
        return True
    elif anio1 < anio2:
        return False

    # Comparar meses si los años son iguales
    if mes1 > mes2:
        return True
    elif mes1 < mes2:
        return False

    # Comparar días si los años y meses son iguales
    return dia1 > dia2

def ordenado(lista: List[float], ascendente: bool) -> bool:
    """
    Verifica si una lista de flotantes está ordenada ascendentemente o descendentemente,
    según el valor de la variable ascendente.

    Parametros:
    - lista (list): Lista de números flotantes.
    - ascendente (bool): True si se debe verificar orden ascendente, False para orden descendente.

    Retorno:
    - bool: True si la lista está ordenada según la condición, False de lo contrario.
    """
    if ascendente:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
    else:
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                return False
    return True

def es_permutacion(lista: List[int], N: int) -> bool:
    """
    Verifica si una lista es una permutación de la secuencia <0, 1, 2, ..., N-1>.

    Parametros:
    - lista (list): Lista de números enteros.
    - N (int): Entero que representa el rango de la secuencia.

    Retorno:
    - bool: True si la lista es una permutación, False de lo contrario.
    """
    if len(lista) != N:
        return False

    # Verificar si la lista contiene todos los elementos de la secuencia
    elementos_presentes: List[int] = set(lista)
    elementos_secuencia: List[int] = set(range(N))

    return elementos_presentes == elementos_secuencia

def suma_maxima(arr: List[int]) -> int:
    """
    Encuentra el segmento [p..q) con la suma máxima posible en un arreglo de números enteros.

    Parametros:
    - arr (list): Lista de números enteros.

    Retorno:
    - int: Suma máxima del segmento [p..q).
    """
    suma: int = 0
    i: int = 0
    r: int = 0

    while i < len(arr):
        r = max(r + arr[i], 0)
        suma = max(suma, r)
        i += 1
    
    return suma

def desviacion_estandar(numeros: List[float]) -> float:
    """
    Calcula la desviación estándar de una lista de flotantes.

    Parametros:
    - numeros (list): Lista de números flotantes.

    Retorno:
    - float: Desviación estándar de los elementos de la lista.
    """
    n: int = len(numeros)

    if n <= 1:
        return 0

    # Calcular la media
    suma_total: float = 0
    for num in numeros:
        suma_total += num
    media: float = suma_total / n

    # Calcular la suma de los cuadrados de las diferencias
    suma_cuadrados_diferencias: float = 0
    for num in numeros:
        suma_cuadrados_diferencias += (num - media) ** 2

    # Calcular la desviación estándar
    desviacion_estandar: float = (suma_cuadrados_diferencias / n) ** 0.5

    return desviacion_estandar

def diferencia_matriz(matriz: List[List[float]], N: int) -> float:
    """
    Calcula la diferencia entre la suma de los elementos de la submatriz NxN en la esquina superior izquierda de M
    y la suma del resto de los elementos.

    Parametros:
    - matriz (list): Matriz cuadrada de números flotantes.
    - N (int): Tamaño de la submatriz cuadrada.

    Retorno:
    - float: Diferencia entre las sumas.
    """
    if len(matriz) != len(matriz[0]) or N > len(matriz):
        return 0

    suma_submatriz: float = 0
    suma_resto: float = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < N and j < N:
                suma_submatriz += matriz[i][j]
            else:
                suma_resto += matriz[i][j]

    return suma_submatriz - suma_resto

def logaritmo(R: int, B: int = 2) -> int:
    """
    Encuentra el mayor número entero P tal que B^P ≤ R.

    Parametros:
    - R (int): Número entero positivo.
    - B (int): Base del logaritmo. Por defecto, B es 2.

    Retorno:
    - int: Mayor número entero P tal que B^P ≤ R.
    """
    P: int = 0
    potencia_B: int = 1

    while potencia_B <= R:
        potencia_B *= B
        P += 1

    return P - 1

def cuadrado_magico(matriz: List[int]) -> bool:
    """
    Determina si una matriz cuadrada de enteros es un cuadrado mágico.

    Parametros:
    - matriz (list): Matriz cuadrada de números enteros.

    Retorno:
    - bool: True si es un cuadrado mágico, False de lo contrario.
    """
    if len(matriz) != len(matriz[0]):
        return False

    n: int = len(matriz)

    # Calcular la suma mágica (la suma de una fila, columna o diagonal)
    suma_magica: int = 0
    for num in matriz[0]:
        suma_magica += num

    # Verificar las filas y columnas
    for i in range(n):
        suma_fila: int = 0
        suma_columna: int = 0
        for j in range(n):
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
        if suma_fila != suma_magica or suma_columna != suma_magica:
            return False

    # Verificar la diagonal principal
    suma_diagonal_principal: int = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
    if suma_diagonal_principal != suma_magica:
        return False

    # Verificar la diagonal secundaria
    suma_diagonal_secundaria: int = 0
    for i in range(n):
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    if suma_diagonal_secundaria != suma_magica:
        return False

    return True
