#Se define la función con la que se va a trabajar
def Funcion(x):
    y = -5 + (1/2)*(0.01*x*x)
    return y

#Utiliza el método de diferencias centradas para encontrar la derivada de la función establecida en Función
def Derivar(x):
    h = 0.01
    derivada = (Funcion(x-2*h) - 8*Funcion(x-h) + 8*Funcion(x+h) - Funcion(x+2*h))/(12*h)
    return derivada

#Se programa el método de Newton Raphson para encontrar los ceros de Funcion además de calcular el error relativo
def NewtonRaphson(x):
    for i in range (1,11):
        x = x - Funcion(x)/Derivar(x)
        print("La aproximación actual es: ", x)
        Error = ((x - ValorTeorico)/ValorTeorico)*100
        print("El error es de: ", Error)
    return x

x = 1
ValorTeorico = 1000**(1/2)
NewtonRaphson(x)






