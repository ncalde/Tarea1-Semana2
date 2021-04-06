# Potencial variable
# Natalia Calderón Barboza

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Variables globales
longitudArista = 1
numTerminos = 5
puntosMalla = 30


def U0(x):
    """
    Se define el potencial eléctrico que existe en el borde de la placa.
    Parámetros:
        x: posición al largo del borde
    Salidas:
        valorU0: valor del potencial en la posición x
    """
    valorU0 = 25 + (75*x)/longitudArista
    return valorU0


def funcion(x,i):
    """
    Función a integrar para encontrar los e.
    Parámetros:
        x: posición al largo del borde
        i: término
    Salidas:
        función evaluada en x,i
    """
    funcion = (25 + (75*x)/longitudArista)*np.sin(i*np.pi*x/longitudArista)
    return funcion

def AproximarUXY(x, y):
    """
    Calcular el valor aproximado del potencial eléctrico en el punto(x,y)
    Parámetros:
        x: posición(es) en el eje x
        y: posición(es) en el eje y
    Salidas:
        valorAproxUXY: valor del potencial eléctrico en el punto(x,y)
    """

    # Se inicializa el valorAproxUXY
    valorAproxUXY = 0

    # Se realiza la sumatoria hasta alcanzar el número de términos solicitado
    for i in range(1, numTerminos+1):
        integral, error = integrate.quad(funcion,0,longitudArista,args=(i))
        print(integral)
        e = integral/(np.sinh(i*np.pi))
        valorAproxUXY += e*np.sin(x*i*np.pi/longitudArista)*np.sinh(y*i*np.pi/longitudArista)
    return valorAproxUXY


def main():
    x = np.linspace(0, longitudArista, puntosMalla)
    y = np.linspace(0, longitudArista, puntosMalla)
    X, Y = np.meshgrid(x, y)
    Z = AproximarUXY(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="spring", edgecolor="none")
    ax.set_title("Aproximación potencial eléctrico en la placa")
    plt.show()


if __name__ == "__main__":
    main()