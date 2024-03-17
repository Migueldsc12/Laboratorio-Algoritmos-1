import tkinter as tk
from typing import Tuple, List


def circulo(canvas: tk.Canvas, x: int, y: int, r: int, c: str) -> int:
    """
    Dibujar un círculo en el canvas y hacer que se mueva 5 píxeles a la derecha cuando se hace clic en él.

    param canvas: El canvas en el que se dibujará el círculo.
    param x: La coordenada x del centro del círculo.
    param y: La coordenada y del centro del círculo.
    param r: El radio del círculo.
    param c: El color del círculo.

    return: El id del círculo que se dibujó.
    """

    # Dibujar el círculo
    id_circulo: int = canvas.create_oval(x-r, y-r, x+r, y+r, fill=c)

    # Mover el círculo cuando se hace clic en él
    canvas.tag_bind(id_circulo, '<Button-1>', lambda e: canvas.move(id_circulo, 5, 0))

    return id_circulo

def cuadrado(canvas: tk.Canvas, x: int, y: int, l: int, c1: str, c2: str) -> int:
    """
    Dibujar un cuadrado en el canvas y cambiar su color cuando el mouse pasa sobre él.

    param canvas: El canvas en el que se dibujará el cuadrado.
    param x: La coordenada x de la esquina superior izquierda del cuadrado.
    param y: La coordenada y de la esquina superior izquierda del cuadrado.
    param l: La longitud de un lado del cuadrado.
    param c1: El color del cuadrado.
    param c2: El color al que se cambiará el cuadrado cuando el mouse pase sobre él.

    return: El id del cuadrado que se dibujó.
    """

    # Dibujar el cuadrado
    id_cuadrado: int = canvas.create_rectangle(x, y, x+l, y+l, fill=c1)

    # Cambiar el color del cuadrado cuando el mouse pasa sobre él
    canvas.tag_bind(id_cuadrado, '<Enter>', lambda e: canvas.itemconfig(id_cuadrado, fill=c2))
    canvas.tag_bind(id_cuadrado, '<Leave>', lambda e: canvas.itemconfig(id_cuadrado, fill=c1))

    return id_cuadrado

def cruz(canvas: tk.Canvas, x: int, y: int, l: int, c: str) -> Tuple[int, int]:
    """
    Dibujar una cruz en el canvas y hacer que desaparezca cuando se hace clic en ella.

    param canvas: El canvas en el que se dibujará la cruz.
    param x: La coordenada x del centro de la cruz.
    param y: La coordenada y del centro de la cruz.
    param l: La longitud de los brazos de la cruz.
    param c: El color de la cruz.

    return: Una tupla con los ids de las dos líneas que forman la cruz.
    """

    # Dibujar las dos líneas que forman la cruz
    id_linea1 = canvas.create_line(x-l/2, y-l/2, x+l/2, y+l/2, fill=c)
    id_linea2 = canvas.create_line(x-l/2, y+l/2, x+l/2, y-l/2, fill=c)

    # Hacer que las líneas desaparezcan cuando se hace clic en ellas
    canvas.tag_bind(id_linea1, '<Button-1>', lambda e: canvas.delete(id_linea1, id_linea2))
    canvas.tag_bind(id_linea2, '<Button-1>', lambda e: canvas.delete(id_linea2, id_linea1))

    return [id_linea1, id_linea2]

def cara(canvas: tk.Canvas, x: int, y: int, c: str) -> List[int]:
    """
    Dibujar una cara en el canvas.

    param canvas: El canvas en el que se dibujará la cara.
    param x: La coordenada x del centro de la cara.
    param y: La coordenada y del centro de la cara.
    param c: El color de la cara.

    return: Una lista con los ids de los elementos que forman la cara.
    """

    # Dibujar los ojos
    id_ojo1: int = canvas.create_oval(x-20, y-20, x-10, y-10, fill=c)
    id_ojo2: int = canvas.create_oval(x+10, y-20, x+20, y-10, fill=c)

    # Dibujar la nariz
    id_nariz: int = canvas.create_line(x, y, x, y+10, fill=c)

    # Dibujar la boca
    id_boca: int = canvas.create_line(x-20, y+20, x+20, y+20, fill=c)

    return [id_ojo1, id_ojo2, id_nariz, id_boca]

def casita(canvas: tk.Canvas, x: int, y: int) -> List[int]:
    """
    Dibujar una casita en el canvas.

    param canvas: El canvas en el que se dibujará la casita.
    param x: La coordenada x de la esquina superior izquierda de la casita.
    param y: La coordenada y de la esquina superior izquierda de la casita.

    return: Una lista con los ids de los elementos que forman la casita.
    """

    # Dibujar la casa
    id_casa: int = canvas.create_rectangle(x, y, x+100, y+100)

    # Dibujar la puerta
    id_puerta: int = canvas.create_rectangle(x+40, y+60, x+60, y+100)

    # Dibujar el pomo de la puerta
    id_pomo: int = canvas.create_oval(x+55, y+80, x+60, y+85, fill='black')

    # Dibujar el techo
    id_techo: int = canvas.create_polygon(x, y, x+100, y, x+50, y-50, fill='red')

    # Dibujar la ventana
    id_ventana: int = canvas.create_rectangle(x+70, y+20, x+90, y+40)

    return [id_casa, id_puerta, id_pomo, id_techo, id_ventana]