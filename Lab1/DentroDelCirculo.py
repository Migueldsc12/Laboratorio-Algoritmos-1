from typing import Union

"""
FUNCION QUE DETERMINA SI UN PUNTO ESTA DENTRO DE UN CIRCULO
ENTRADA: RADIO DEL CIRCULO, COORDENADA X DEL PUNTO, COORDENADA Y DEL PUNTO
SALIDA: BOOLEANO QUE INDICA SI EL PUNTO ESTA DENTRO DEL CIRCULO O NO
"""
def dentro_del_circulo(radio: float, x: float, y: float) -> Union[bool, str]:
    if radio < 0:
        return "El radio del círculo debe ser no negativo."
    
    distancia_al_centro = (x**2 + y**2)**0.5
    
    return distancia_al_centro <= radio

"""
FUNCION MAIN QUE PIDE EL RADIO DEL CIRCULO Y LAS COORDENADAS DEL PUNTO
ENTRADA: RADIO DEL CIRCULO, COORDENADA X DEL PUNTO, COORDENADA Y DEL PUNTO
SALIDA: BOOLEANO QUE INDICA SI EL PUNTO ESTA DENTRO DEL CIRCULO O NO
"""
def main() -> None:
    try:
        radio = float(input("Ingrese el radio del círculo: \n"))
        x = float(input("Ingrese la coordenada x del punto: \n"))
        y = float(input("Ingrese la coordenada y del punto: \n"))
        
        resultado = dentro_del_circulo(radio, x, y)

        if (resultado):
            print(resultado)
        else:
            print(resultado)

    except ValueError:
        print("Ingrese números reales válidos.")

if __name__ == "__main__":
    main()
