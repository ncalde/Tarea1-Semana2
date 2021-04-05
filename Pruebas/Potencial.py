import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def U0(x):
    """
    Se define el potencial eléctrico que existe en el borde de la placa.
    Parámetros:
        x: posición al largo del borde
    Salidas:
        valorU0: valor del potencial en la posición x
    """
    valorU0 = 100
    return valorU0


def AproximarUXY(x, y, lado, N):
    """
    Calcular el valor aproximado del potencial eléctrico en el punto(x,y)
    Parámetros:
        x: posición en el eje x
        y: posición en el eje y
        lado: arista de la placa cuadrada sujeta al potencial eléctrico
        N: número de términos que tendrá el cálcul del potencial (mayor o igual a 1)
    Salidas:
        valorAproxUXY: valor del potencial eléctrico en el punto(x,y)
    """

    # Se inicializa el valorAproxUXY
    valorAproxUXY = 0

    # Se realiza la sumatoria hasta alcanzar el número de términos solicitado
    for i in range(0, N):
        nImpar = 2 * i + 1
        valorAproxUXY += (4 * U0(x) / (nImpar * np.pi)) * np.sin(nImpar * np.pi * x / lado) \
                         * np.sinh(nImpar * np.pi * y / lado) / np.sinh(nImpar * np.pi)
    return valorAproxUXY


def main():
    lado = 4
    numTerminos = 10
    x = 2.1
    y = 1.7
    u = AproximarUXY(x, y, lado, numTerminos)
    print(u)

if __name__ == "__main__":
    main()