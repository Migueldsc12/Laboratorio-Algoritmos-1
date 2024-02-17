# Examen 1 - Algoritmos y Estructuras 1
# Miguel Salomon - 1910274

from typing import List

def mostrar_menu() -> None:
    """
    Muestra el menú principal del programa.

    Retorna:
    - None
    """
    print("\nIndique una opción:")
    print("1) Crear contacto")
    print("2) Mostrar contactos")
    print("3) Editar contacto")
    print("4) Eliminar contacto")
    print("5) Buscar contacto")
    print("6) Salir")

def crear_contacto(agenda: List[str]) -> None:
    """
    Crea un nuevo contacto y lo agrega a la agenda.

    Parametros:
    - agenda: Lista. La agenda de contactos.

    Retorna:
    - None
    """
    while True:
        nombre: str = input("Nombre: ")
        if nombre:
            break
        else:
            print("Nombre inválido. El nombre debe tener al menos un carácter.")

    while True:
        apellido: str = input("Apellido: ")
        if apellido:
            break
        else:
            print("Apellido inválido. El apellido debe tener al menos un carácter.")

    while True:
        telefono: str = input("Telefono (formato XXXX-XXXXXXX): ")
        if telefono_valido(telefono):
            break
        else:
            print("Número de teléfono inválido. Debe seguir el formato XXXX-XXXXXXX.")

    nuevo_contacto = {'Nombre': nombre, 'Apellido': apellido, 'Teléfono': telefono}
    agenda.append(nuevo_contacto)
    print("Contacto creado exitosamente.")

def telefono_valido(telefono: str) -> bool:
    """
    Verifica que el número de teléfono siga el formato XXXX-XXXXXXX.
    
    Parametros:
    - telefono: str. El número de teléfono a verificar.
    
    Retorna:
    - bool. True si el número de teléfono sigue el formato, False de lo contrario.
    """
    # Verificar que el número de teléfono siga el formato XXXX-XXXXXXX
    partes: List[str] = telefono.split('-')
    return len(partes) == 2 and partes[0].isdigit() and len(partes[0]) == 4 and partes[1].isdigit() and len(partes[1]) == 7

def mostrar_contactos(agenda: List[str]) -> None:
    """
    Muestra los contactos en la agenda.
    
    Parametros:
    - agenda: Lista. La agenda de contactos.
    
    Retorna:
    - None
    """
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        i = 0
        for contacto in agenda:
            print(f"\n{i} | Nombre: {contacto['Nombre']} | Apellido: {contacto['Apellido']} | Teléfono: {contacto['Teléfono']}\n")
            i += 1

def editar_contacto(agenda: List[str]) -> None:
    """
    Edita un contacto de la agenda.
    
    Parametros:
    - agenda: Lista. La agenda de contactos.
    
    Retorna:
    - None
    """
    if not agenda:
        print("No hay contactos para editar.")
        return
    
    while True:
        try:
            indice: int = int(input("Ingrese el número del contacto que desea editar: "))
            if 0 <= indice <= len(agenda):
                break
            else:
                print("Número de contacto no válido.")
        except ValueError:
            print("Ingrese un número válido.")

    contacto: str = agenda[indice]
    
    print("Deje en blanco los campos que no desea cambiar.")

    nuevo_nombre: str = input(f"Nuevo nombre ({contacto['Nombre']}): ") or contacto['Nombre']
    nuevo_apellido: str = input(f"Nuevo apellido ({contacto['Apellido']}): ") or contacto['Apellido']
    nuevo_telefono: str = input(f"Nuevo teléfono ({contacto['Teléfono']}): ") or contacto['Teléfono']

    contacto['Nombre'] = nuevo_nombre
    contacto['Apellido'] = nuevo_apellido
    contacto['Teléfono'] = nuevo_telefono

    print("Contacto editado exitosamente.")

def eliminar_contacto(agenda: List[str]) -> None:
    """
    Elimina un contacto de la agenda.
    
    Parametros:
    - agenda: Lista. La agenda de contactos.

    Retorna:
    - None
    """
    if not agenda:
        return
    try:
        indice: int = int(input("Ingrese el número del contacto que desea eliminar: "))
        if 0 <= indice < len(agenda):
            contacto_eliminado = agenda.pop(indice)
            print(f"Contacto {contacto_eliminado['Nombre']} eliminado exitosamente.")
        else:
            print("Número de contacto no válido.")
    except ValueError:
        print("Ingrese un número válido.")

def buscar_contacto(agenda: List[str]) -> None:
    """
    Busca contactos en la agenda que coincidan con un criterio de búsqueda.
    
    Parametros:
    - agenda: Lista. La agenda de contactos.

    Retorna:
    - None
    """
    if not agenda:
        print("No hay contactos para buscar.")
        return

    criterio_busqueda: str = input("Ingrese el criterio de búsqueda: ").lower()
    tokens: List[str] = criterio_busqueda.split()

    resultados: List[str] = []
    for contacto in agenda:
        if any(token in contacto['Nombre'].lower() or
               token in contacto['Apellido'].lower() or
               token in contacto['Teléfono'] for token in tokens):
            resultados.append(contacto)

    if resultados:
        print("Resultados de la búsqueda:")
        mostrar_contactos(resultados)
    else:
        print("No se encontraron contactos que coincidan con el criterio de búsqueda.")

def main() -> None:
    """
    Función principal del programa. Muestra el menú y maneja la lógica del programa.

    Retorna:
    - None
    """
    agenda: List[str] = []
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == '1':
            crear_contacto(agenda)
        elif opcion == '2':
            mostrar_contactos(agenda)
        elif opcion == '3':
            editar_contacto(agenda)
        elif opcion == '4':
            eliminar_contacto(agenda)
        elif opcion == '5':
            buscar_contacto(agenda)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")

if __name__ == "__main__":
    main()
