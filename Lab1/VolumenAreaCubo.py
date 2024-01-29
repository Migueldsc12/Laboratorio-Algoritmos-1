from typing import Tuple

"""
FUNCION QUE CALCULA EL VOLUMEN Y EL AREA SUPERFICIAL DE UN CUBO
ENTRADA: LADO DEL CUBO
SALIDA: VOLUMEN Y AREA SUPERFICIAL DEL CUBO
"""
def calcular_volumen_area_cubo(lado: float) -> Tuple[float, float]:
    if lado >= 0:
        volumen = lado ** 3
        area_superficial = 6 * lado ** 2
        return volumen, area_superficial
    else:
        raise ValueError("El número debe ser no negativo.")

"""
FUNCION MAIN QUE PIDE EL LADO DEL CUBO Y LLAMA A LA FUNCION QUE CALCULA EL VOLUMEN Y EL AREA SUPERFICIAL
ENTRADA: LADO DEL CUBO
SALIDA: VOLUMEN Y AREA SUPERFICIAL DEL CUBO
"""
def main() -> None:
    try:
        lado = float(input("Indique el lado del cubo: \n"))
        volumen, area_superficial = calcular_volumen_area_cubo(lado)

        print(volumen, area_superficial)

    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
