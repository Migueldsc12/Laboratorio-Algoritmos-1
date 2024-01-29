from typing import Union

"""
FUNCION QUE DETERMINA SI UN AÑO ES BISIESTO
ENTRADA: AÑO
SALIDA: BOOLEANO QUE INDICA SI EL AÑO ES BISIESTO O NO
"""
def es_bisiesto(anio: int) -> Union[bool, str]:
    if 1900 <= anio <= 2200:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return True
        else:
            return False
    else:
        return "El año debe estar en el rango [1900, 2200]."

"""
FUNCION MAIN QUE PIDE EL AÑO A VERIFICAR
ENTRADA: AÑO
SALIDA: BOOLEANO QUE INDICA SI EL AÑO ES BISIESTO O NO
"""
def main() -> None:
    try:
        anio = int(input("Ingrese el año a verificar: \n"))
        resultado = es_bisiesto(anio)

        if (resultado):
            print(resultado)
        else:
            print(resultado)

    except ValueError:
        print("Ingrese un número entero válido.")

if __name__ == "__main__":
    main()
