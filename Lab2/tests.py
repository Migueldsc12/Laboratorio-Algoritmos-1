from typing import List, Tuple
from LabSem3 import (
    buscar,
    es_primo,
    promedio,
    son_amigos,
    suma_maximo,
    es_simetrica,
    esta_ordenado,
    es_palindromo,
    suma_cuadrado_impares,
)


def test_es_primo() -> float:
    """
    Casos de prueba para la función es_primo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"Testing \033[1mes_primo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, bool]] = [
        (2, True),
        (3, True),
        (67, True),
        (1000003, True),
        (1, False),
        (68, False),
        (69, False),
        (942841, False),
    ]

    for test in test_cases:
        try:
            test_result: float = es_primo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_suma_cuadrado_impares() -> float:
    """
    Casos de prueba para la función suma_cuadrado_impares.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1msuma_cuadrado_impares\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, int]] = [
        (1, 0),
        (2, 1),
        (3, 1),
        (10, 165),
        (100, 166650),
        (101, 166650),
        (1000, 166666500),
    ]

    for test in test_cases:
        try:
            test_result: float = suma_cuadrado_impares(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_son_amigos() -> float:
    """
    Casos de prueba para la función son_amigos.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mson_amigos\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, int, bool]] = [
        (220, 284, True),
        (1184, 1210, True),
        (2620, 2924, True),
        (5020, 5564, True),
        (6232, 6368, True),
        (10744, 10856, True),
        (220, 221, False),
        (1184, 1504, False),
        (2620, 2925, False),
        (4803, 5565, False),
        (6232, 6369, False),
        (12285, 29190, False),
        (10857, 10744, False),
    ]

    for test in test_cases:
        try:
            test_result: float = son_amigos(test[0], test[1])

            if test_result == test[2]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[2]}")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}, {test[1]}")
            print(f"Expected: {test[2]}")

    return result / len(test_cases)


def test_esta_ordenado() -> float:
    """
    Casos de prueba para la función esta_ordenado.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mesta_ordenado\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], bool]] = [
        ([], True),
        ([-10.0], True),
        ([-10000.0, -100.5, -11.9, -2.1, -1.0], True),
        ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 5.0000000001, 6.0, 7.0, 8.0, 9.0], True),

        ([5.0, 4.0, 3.0, 2.0, 1.0], False),
        ([0.0, 0.0, 0.0, 0.0, -0.0000001, 0.0, 0.0, 0.0, 0.0], False),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 4.999999, 6.0, 7.0, 8.0, 9.0], False),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 5.0000001, 6.0, 7.0, 8.0, 7.99999999999], False),
    ]

    for test in test_cases:
        try:
            test_result: float = esta_ordenado(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_buscar() -> float:
    """
    Casos de prueba para la función buscar.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mbuscar\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], float, int]] = [
        ([], 0.0, -1),
        ([1.0], 1.0, 0),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0, 2),
        ([0.0, 0.0, 0.0, 0.0, 0.0], 0.0, 0),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 9.0, 8),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 10.0, -1),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 5.000001, -1),
        ([1.0, 2.0, 3.0, 4.0, 5.000001, 6.0, 7.0, 8.0, 9.0], 5.000001, 4),
    ]

    for test in test_cases:
        try:
            test_result: float = buscar(test[0], test[1])

            if test_result == test[2]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[2]}")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}, {test[1]}")
            print(f"Expected: {test[2]}")

    return result / len(test_cases)


def test_promedio() -> float:
    """
    Casos de prueba para la función promedio.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mpromedio\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], float]] = [
        ([1.0], 1.0),
        ([1.0, 2.0], 1.5),
        ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ([-1.0, -2.0, -3.0, -4.0, -5.0], -3.0),
        ([-1.0, 2.0, -3.0, 4.0, -5.0], -0.6),
        ([1.1, 2.2, 3.3, 4.4, 5.5], 3.3),
    ]

    for test in test_cases:
        try:
            test_result: float = promedio(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_es_palindromo() -> float:
    """
    Casos de prueba para la función es_palindromo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mes_palindromo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[str, bool]] = [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("abba", True),
        ("abcba", True),
        ("abccba", True),
        ("abcdcba", True),
        ("abcddadcba", False),
        ("abcdeedcba", True),
        ("abcdeddcba", False),
    ]

    for test in test_cases:
        try:
            test_result: float = es_palindromo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_suma_maximo() -> float:
    """
    Casos de prueba para la función suma_maximo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1msuma_maximo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[List[int]], int]] = [
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            18
        ),
        (
            [],
            0
        ),
        (
            [[], [], []],
            0
        ),
        (
            [[1]],
            1
        ),
        (
            [[1, 2, 3, 4, 5]],
            5
        ),
        (
            [[1], [2], [3], [4], [5]],
            15
        ),
        (
            [[-1, -2, -3],
             [-4, -5, -6],
             [-7, -8, -9]],
            -12
        ),
        (
            [[0, 0, 0],
             [0, -1, -2],
             [-3, -4, -5]],
            -3
        ),
        (
            [[1, -2, 3],
             [-4, -5, -6],
             [7, -8, 9]],
            8
        ),
    ]
    for test in test_cases:
        try:
            test_result: float = suma_maximo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_es_simetrica() -> float:
    """
    Casos de prueba para la función es_simetrica.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mes_simetrica\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[List[int]], bool]] = [
        (
            [],
            True
        ),
        (
            [[1]],
            True
        ),
        (
            [[1, 2],
             [2, 1]],
            True
        ),
        (
            [[1, 2],
             [3, 4]],
            False
        ),
        (
            [[1, 2, 3],
             [2, 4, 5],
             [3, 5, 6]],
            True
        ),
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            False
        ),
        (
            [[-1, -2, -3],
             [-2, -4, -5],
             [-3, -5, -6]],
            True
        ),
        (
            [[0, 0, 0],
             [0, -1, -2],
             [0, -2, -1]],
            True
        ),
        (
            [[1, -2, 3],
             [-2, 4, -5],
             [3, 5, 6]],
            False
        ),
    ]

    for test in test_cases:
        try:
            test_result: float = es_simetrica(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def main() -> None:
    """
    Función principal.
    """
    result: float = 0.0

    print("\033[1mCorriendo tests...\033[0m")
    result += test_es_primo()
    result += test_suma_cuadrado_impares()
    result += test_son_amigos()
    result += test_esta_ordenado()
    result += test_buscar()
    result += test_promedio()
    result += test_es_palindromo()
    result += test_suma_maximo()
    result += test_es_simetrica()

    print(f"---\n{result * 5 / 9}/5.0 Puntaje total.")


if __name__ == "__main__":
    main()
