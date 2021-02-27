#Importación de librerías

import scipy.integrate

#Definición de funciones

def PesoWi(posicion,numIntervalos):
    """
    Recibe la posición del punto y el número de intervalos (número de puntos + 1)
    Devuelve el peso de cada término de la sumatoria que utiliza Simpson
    """
    if posicion == 0 or posicion == (numIntervalos):
        return 1
    elif (posicion % 2) == 0:
        return 2
    else:
        return 4


def IntegrarSimpson(limiteInferior, limiteSuperior, numIntervalos):
    """
    Recibe los límites de integración y el número de intervalos a utilizar en la aproximación
        numIntervalos debe ser un número natural múltiplo de 3
    Aproxima una integral definida con el método Simpson
    """
    sumatoria = 0.0
    espaciamiento = (limiteSuperior - limiteInferior) / numIntervalos
    # Se agregan a la sumatoria los valores multiplicados por su peso
    for iPosicion in range(0, numIntervalos + 1):
        xi = limiteInferior + espaciamiento * iPosicion
        sumatoria = sumatoria + PesoWi(iPosicion, numIntervalos) * F(xi)
    integral = (espaciamiento * sumatoria) / 3
    return integral


def F(x):
    """
    Recibe x
    Devuelve el valor de f(x), esto es x evaluado en la función a integrar
    """
    return 0.005*x + 0.5



def main():
    limiteInferior = 0
    limiteSuperior = 100
    numIntervalos = [3, 9, 27, 81, 243]
    #Se llama a la función integrarSimpson con 5 valores distintos para numIntervalos
    for i in numIntervalos:
        integralSimpson = IntegrarSimpson(limiteInferior, limiteSuperior, i)
        # Se va a utilizar la función scipy.integrate para obtener el valor exacto de la integral y calcular el error
        integralScipy, errorScipy = scipy.integrate.quad(F, limiteInferior, limiteSuperior)
        error = (integralScipy - integralSimpson) * 100 / integralScipy
        print("Integral calculada con", i, "subintervalos: ", integralSimpson, "    error:", error, "%")


if __name__ == '__main__':
    main()

