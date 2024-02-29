import math
from typing import List

def numero_de_kaprekar(n: int): 
    if n == 1 : 
        return True
      
    sq_n: int = n * n 
    count_digits: int = 1
    while not sq_n == 0 : 
        count_digits = count_digits + 1
        sq_n = sq_n // 10
      
    sq_n = n*n  
      
    r_digits: int = 0
    while r_digits< count_digits : 
        r_digits = r_digits + 1
        eq_parts: int = (int) (math.pow(10, r_digits)) 
          
        if eq_parts == n : 
            continue
          
          
        sum: int = sq_n//eq_parts + sq_n % eq_parts 
        if sum == n : 
            return True
      
    return False

def numero_feliz(n: int) -> bool:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un número entero positivo.")

    if n == 1 or n == 7:
        return True
          
    Sum: int = n
    x: int = n
  
    while Sum > 9:
        Sum = 0
          
        while x > 0:
            d = x % 10
            Sum += d * d
            x = int(x / 10)
         
        if Sum == 1:
            return True
              
        x = Sum
     
    if Sum == 7:
        return True
          
    return False

def anagrama(cadena1: List[str], cadena2: List[str]) -> bool:
    # Verifica si las cadenas tienen la misma longitud
    if len(cadena1) != len(cadena2):
        return False

    # Convierte las cadenas en listas de caracteres
    lista_cadena1: List[str] = list(cadena1)
    lista_cadena2: List[str] = list(cadena2)

    # Ordena las listas de caracteres
    lista_cadena1.sort()
    lista_cadena2.sort()

    # Compara si las listas ordenadas son iguales
    return lista_cadena1 == lista_cadena2


def comprimir(s) -> str:
    # Verifica si el string contiene caracteres numéricos
    if any(char.isdigit() for char in s):
        raise ValueError("El string no debe contener caracteres numéricos.")

    resultado: str = ""
    i: int = 0

    while i < len(s):
        # Token actual y cantidad de ocurrencias
        token = s[i]
        count = 1

        # Busca ocurrencias consecutivas del mismo token
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1

        # Agrega el resultado al string comprimido
        resultado += str(count) + token

        i += 1

    return resultado

def puede_colocar_flores(maceta: List[int], n: int) -> bool:
    # Verificaciones
    if n < 0:
        raise ValueError("El número de flores a plantar debe ser no-negativo.")
    
    if any(valor not in [0, 1] for valor in maceta):
        raise ValueError("Los valores de la maceta deben ser 0 o 1.")

    # Inicializa el contador de flores plantadas
    flores_plantadas: int = 0
    i: int = 0

    while i < len(maceta):
        # Verifica si la parcela actual y sus vecinas están vacías
        if maceta[i] == 0 and (i == 0 or maceta[i - 1] == 0) and (i == len(maceta) - 1 or maceta[i + 1] == 0):
            # Planta una flor
            flores_plantadas += 1
            i += 2  # Salta a la siguiente parcela vacía
        else:
            i += 1  # Avanza a la siguiente parcela

    return flores_plantadas >= n

def sopa_de_letras(palabra: str, matriz: List[List[str]]) -> bool:
    def buscar_palabra(palabra, fila, columna, direccion):
        dx, dy = direccion
        x, y = fila, columna

        for letra in palabra[1:]:
            x += dx
            y += dy

            if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]) and matriz[x][y].upper() == letra:
                continue
            else:
                return False

        return True

    # Verificaciones
    if not all(isinstance(fila, list) and all(isinstance(c, str) and len(c) == 1 for c in fila) for fila in matriz):
        raise ValueError("La matriz solo puede contener caracteres (strings de longitud 1).")

    if not matriz or not all(len(fila) == len(matriz[0]) for fila in matriz):
        raise ValueError("La matriz debe ser M x N para algún M, N enteros.")

    # Convertir la palabra a mayúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
    palabra = palabra.upper()

    # Recorrer la matriz para buscar la palabra
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j].upper() == palabra[0]:
                # Direcciones para buscar la palabra (horizontal, vertical, diagonal)
                direcciones = [(0, 1), (1, 0), (1, 1), (-1, 1)]

                for direccion in direcciones:
                    if buscar_palabra(palabra, i, j, direccion):
                        return True

    return False

def jaque(posicion_rey: List[int], posiciones_torres: List[int], posiciones_alfiles: List[int]) -> bool:
    # Verificaciones
    if not (0 <= posicion_rey[0] < 8 and 0 <= posicion_rey[1] < 8):
        raise ValueError("La posición del rey debe pertenecer al conjunto [0, 8) x [0, 8).")

    if posicion_rey in posiciones_torres or posicion_rey in posiciones_alfiles:
        raise ValueError("El rey no puede ocupar la misma posición que otra pieza.")

    for posicion in posiciones_torres + posiciones_alfiles:
        if not (0 <= posicion[0] < 8 and 0 <= posicion[1] < 8):
            raise ValueError("Todas las posiciones deben pertenecer al conjunto [0, 8) x [0, 8).")

    # Verificar jaque por torres
    for posicion_torre in posiciones_torres:
        if posicion_torre[0] == posicion_rey[0] or posicion_torre[1] == posicion_rey[1]:
            return True

    # Verificar jaque por alfiles
    for posicion_alfil in posiciones_alfiles:
        if abs(posicion_alfil[0] - posicion_rey[0]) == abs(posicion_alfil[1] - posicion_rey[1]):
            return True

    return False
