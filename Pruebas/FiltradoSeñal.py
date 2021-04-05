import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def main():
    # Parámetros
    tasaMuestreo = 1024
    deltaT = 1

    # Tamaño del arreglo de muestras
    nPuntos = deltaT*tasaMuestreo

    puntosTiempo = np.linspace(0, deltaT, nPuntos)

    frec_1 = 75
    magnitud_1 = 25

    frec_2 = 250
    magnitud_2 = 40

    # Señales
    señal1 = magnitud_1*np.sin(2*np.pi*frec_1*puntosTiempo)
    señal2 = magnitud_2*np.sin(2*np.pi*frec_2*puntosTiempo)


    # Ruido para la señal
    ruido = np.random.normal(0, 13, nPuntos)

    señalPura = señal1 + señal2
    señalRuidosa = señal1 + señal2 + ruido

    fig, (ax1, ax2) = plt.subplots(1, 2, dpi=120, sharey= True)
    ax1.plot(puntosTiempo[0:50], señalPura[0:50])
    ax1.set_title('Señal original')
    ax1.set_xlabel('Tiempo')
    ax1.set_ylabel('Amplitud')

    ax2.plot(puntosTiempo[1:50], señalRuidosa[1:50])
    ax2.set_title('Señal ruidosa')
    ax2.set_xlabel('Tiempo')

    plt.show()

    #==============================================

    # Aplicación de la transformada

    puntosFrecuencia = np.linspace (0.0, 512, int(nPuntos/2))

    # Se aplica la transformada rapida a la señal
    transformadaSeñal = fft(señalRuidosa)
    # print(transformadaSeñal)

    amplitudes = (2/nPuntos)*np.abs(transformadaSeñal[0:np.int(nPuntos/2)])

    fig, ax = plt.subplots(dpi=120)
    ax.plot(puntosFrecuencia, amplitudes)
    ax.set_title('Señal en el dominio de la frecuencia')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('Amplitud')
    ax.set_xticks(np.arange(0,501,50))
    plt.show()

    #==============================================

    # Filtrado de la señal

    limite = 5
    transformadaSeñalFiltrada = transformadaSeñal

    for i in range(len(amplitudes)):
        if amplitudes[i] < limite:
            transformadaSeñalFiltrada[i] = 0+0j

    amplitudesFiltradas = (2/nPuntos)*np.abs(transformadaSeñalFiltrada[0:np.int(nPuntos/2)])


    fig, ax = plt.subplots(dpi=120)
    ax.plot(puntosFrecuencia, amplitudesFiltradas)
    ax.set_title('Señal en el dominio de la frecuencia')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('Amplitud')
    ax.set_xticks(np.arange(0,501,50))
    plt.show()

    #=============================================

    # Aplicación de la transformada inversa y
    # comparación con la señal original

    transformadaInversa = ifft(transformadaSeñalFiltrada)

    fig, (ax1,ax2) = plt.subplots(1, 2, dpi=120, sharey=True)
    ax1.plot(puntosTiempo[0:50], señalPura[0:50])
    ax1.set_title('Señal pura')
    ax1.set_xlabel('Tiempo')
    ax1.set_ylabel('Amplitud')
    ax2.plot(puntosTiempo[1:50], transformadaInversa[1:50])
    ax2.set_title('Señal filtrada')
    ax2.set_xlabel('Tiempo')

    plt.show()

    print(len(amplitudes))
    print(len(transformadaSeñalFiltrada))


if __name__ == '__main__':
    main()

