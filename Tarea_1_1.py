import numpy as np
import scipy.integrate

def PesoWi(i,numIntervalos):
    """
    Devuelve el peso de cada término de la sumatoria que utiliza Simpson
    Los extremos tienen un peso igual a 1
    Los valores intermedios tienen un peso igual a 2 si son múltiplos de 2 y un peso de 4 en caso contrario
    """
    if i == 0 or i == (numIntervalos):
        return 1
    elif (i % 2) == 0:
        return 2
    else:
        return 4

def IntegrarSimpson38(limiteInferior, limiteSuperior, numIntervalos):
    """
    Recibe los límites de integración y el número de intervalos a utilizar en la aproximación
    Aproxima una integral definida con el método Simpson
    """
    sumatoria = 0.0
    espaciamiento = (limiteSuperior - limiteInferior) / numIntervalos
    for i in range(0, numIntervalos + 1):  # Se agregan a la sumatoria los valores multiplicados por su peso
        xi = limiteInferior + espaciamiento * i
        sumatoria = sumatoria + PesoWi(i, numIntervalos) * F(xi)
    integral = (espaciamiento * sumatoria) / 3
    return integral

def F(x):
    """
    Devuelve el valor de f(x), x evaluado en la función a integrar
    """
    return 0.005*x + 0.5

def main():
    limiteInferior = 0
    limiteSuperior = 100
    numIntervalos = [3, 9, 27, 81, 243]
    for i in numIntervalos:
        integralSimpson = IntegrarSimpson38(limiteInferior, limiteSuperior, i)
        # Se va a utilizar la función scipy.integrate para obtener el valor exacto de la integral y calcular el error
        integralScipy, errorScipy = scipy.integrate.quad(F, limiteInferior, limiteSuperior)
        error = (integralScipy - integralSimpson) * 100 / integralScipy
        print("Integral calculada con", i, "subintervalos: ", integralSimpson, "    error:", error, "%")


if __name__ == '__main__':
    main()

