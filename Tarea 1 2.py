#Se definen la funciones con la que se va a trabajar

def Funcion(x):
    """
    Recibe un número x
    Devuelve el valor de f(x), definida a partir de las condiciones del problema
    """
    y = -5 + (1/2)*(0.01*x*x)
    return y


def Derivar(x):
    """
    Recibe un número x
    Devuelve la derivada de la función definida en Funcion(x) mediante el método de diferencias centradas
    """
    h = 0.01
    derivada = (Funcion(x-2*h) - 8*Funcion(x-h) + 8*Funcion(x+h) - Funcion(x+2*h))/(12*h)
    return derivada


def NewtonRaphson(x):
    """
    Recibe un número x, esta es la aproximación inicial determinada arbitrariamente
    Imprime las aproximaciones del cero de la función por el método iterativo de Newton Raphson, con su error relativo
    Devuelve la última aproximación obtenida
    """
    for i in range (1,11):
        x = x - Funcion(x)/Derivar(x)
        print("La aproximación actual es: ", x)
        Error = ((x - ValorTeorico)/ValorTeorico)*100
        print("El error es de: ", Error)
    return x

#Main

x = 1
ValorTeorico = 1000**(1/2)
NewtonRaphson(x)






