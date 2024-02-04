from typing import Union

"""
FUNCION QUE CALCULA EL MAXIMO COMUN DIVISOR DE DOS NUMEROS
ENTRADA: DOS NUMEROS ENTEROS
SALIDA: MAXIMO COMUN DIVISOR DE LOS DOS NUMEROS
"""
def mcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

"""
FUNCION QUE DETERMINA SI DOS NUMEROS SON COPRIMOS
ENTRADA: DOS NUMEROS ENTEROS
SALIDA: BOOLEANO QUE INDICA SI LOS DOS NUMEROS SON COPRIMOS O NO
"""
def son_numeros_coprimos(num1: int, num2: int) -> Union[bool, str]:
    if num1 > 0 and num2 > 0:
        return mcd(num1, num2) == 1
    else:
        return "Ambos números deben ser positivos."

"""
FUNCION MAIN QUE PIDE LOS DOS NUMEROS A VERIFICAR
ENTRADA: DOS NUMEROS ENTEROS
SALIDA: BOOLEANO QUE INDICA SI LOS DOS NUMEROS SON COPRIMOS O NO
"""
def main() -> None:
    try:
        num1: int = int(input("Ingrese el primer número entero: \n"))
        num2: int = int(input("Ingrese el segundo número entero: \n"))
        resultado: int = son_numeros_coprimos(num1, num2)

        print(resultado)

    except ValueError:
        print("Ingrese números enteros válidos.")

if __name__ == "__main__":
    main()
