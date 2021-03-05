# Importación de librerías

import scipy.integrate


# Definición de funciones

def PesoWi(posicion, numIntervalos):
    """
    Recibe la posición del término a la que se le va a determinar el peso y el número de intervalos (número de puntos + 1)
    Devuelve el peso del término según la regla de Simpson
    """
    if posicion == 0 or posicion == (numIntervalos):
        return 1
    elif (posicion % 2) == 0:
        return 2
    else:
        return 4


def IntegrarSimpson(limiteInferior, limiteSuperior, numIntervalos):
    """
    Recibe los límites de integración inferior y superior, y el número de intervalos a utilizar en la aproximación
        * numIntervalos debe ser un número natural múltiplo de 2
    Devuelve la aproximación de una integral definida, obtenida con el método de Simpson
    """
    sumatoria = 0.0
    espaciamiento = (limiteSuperior - limiteInferior) / numIntervalos

    for iPosicion in range(0, numIntervalos + 1):
        # Se calcula el nuevo punto
        xi = limiteInferior + espaciamiento * iPosicion
        # Se agrega a la sumatoria su valor multiplicado por su peso
        sumatoria = sumatoria + PesoWi(iPosicion, numIntervalos) * F(xi)
    integral = (espaciamiento * sumatoria) / 3
    return integral


def F(x):
    """
    Recibe un número x
    Devuelve el valor de f(x), esto es x evaluado en la función a integrar
    """
    return 0.005 * x + 0.5


def main():
    # Se definen los límites según las condiciones del problema
    limiteInferior = 0
    limiteSuperior = 100
    numIntervalos = [2, 4, 8, 16, 32]
    # Se llama a la función integrarSimpson con 5 valores distintos para el parámetro numIntervalos
    for i in numIntervalos:
        integralSimpson = IntegrarSimpson(limiteInferior, limiteSuperior, i)
        # Se va a utilizar la función scipy.integrate para obtener el valor exacto de la integral y calcular el error
        integralScipy, errorScipy = scipy.integrate.quad(F, limiteInferior, limiteSuperior)
        error = (integralScipy - integralSimpson) * 100 / integralScipy
        print("Integral calculada con", i, "subintervalos: ", integralSimpson, "    error:", error, "%")


if __name__ == '__main__':
    main()
