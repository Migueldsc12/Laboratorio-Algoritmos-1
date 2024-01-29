from typing import Union

"""
FUNCION QUE DETERMINA SI UN NUMERO ES CUADRADO PERFECTO
ENTRADA: NUMERO
SALIDA: BOOLEANO QUE INDICA SI EL NUMERO ES CUADRADO PERFECTO O NO
"""
def es_cuadrado_perfecto(numero: int) -> Union[bool, str]:
    if numero >= 0:
        raiz_cuadrada = int(numero**0.5)
        return raiz_cuadrada**2 == numero
    else:
        return "El número debe ser no negativo."

"""
FUNCION MAIN QUE PIDE EL NUMERO A VERIFICAR
ENTRADA: NUMERO
SALIDA: BOOLEANO QUE INDICA SI EL NUMERO ES CUADRADO PERFECTO O NO
"""
def main() -> None:
    try:
        numero = int(input("Ingrese el número a verificar: \n"))
        resultado = es_cuadrado_perfecto(numero)

        if (resultado):
            print(resultado)
        else:
            print(resultado)

    except ValueError:
        print("Ingrese un número entero válido.")

if __name__ == "__main__":
    main()
