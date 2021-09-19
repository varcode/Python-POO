class Vehiculo():
    #Si tiene tanque de nafta es true
    __tanque_de_nafta = True
    __asientos = 0
    __mensaje = ''

    def __init__(self):
        self.__mensaje = 'Se inicio el constructor'

    def __init__(self, tanque_de_nafta):
        self.__mensaje = 'Se inicio el constructor 2'
        self.__tanque_de_nafta = tanque_de_nafta


    def desplazamiento(self):
        print('El vehiculo se esta moviendo')
    
    def detenerse(self):
        print('El vehiculo se detiene')

    def mostrarMensaje(self):
        return self.__mensaje

class Auto(Vehiculo):
    __cantidad_ruedas = 4
    __volante = True
    __asientos = 0
    __cenicero = True
    __capacidad_combustible_litros = 0
    __km_recorridos_total = 0
    __km_recorridos_trayecto = 0
    __caballos_fuerza_motor = 1.0
    __cantidad_combustible = 0

    def __init__(self, capacidad_combustible):
        self.__capacidad_combustible_litros = capacidad_combustible
        self.__mensaje = 'Constructor capacidad combustible'
    
    def __init__(self, capacidad_combustible, motor):
        self.__capacidad_combustible_litros = capacidad_combustible
        self.__caballos_fuerza_motor = motor


    def Arrancar(self):
        self.__km_recorridos_trayecto = 0

    def Detenerse(self):
        self.__km_recorridos_total = self.__km_recorridos_total + self.__km_recorridos_trayecto
    
    def Moverse(self, km_recorridos):
        self.__km_recorridos_trayecto = self.__km_recorridos_trayecto + km_recorridos

    def MostrarCantidadCombustible(self):
        print(self.__cantidad_combustible)

#Volkswagen Up!
miAuto = Auto(50)
#Volkswagen Suran
autoVictor = Auto(30)

miAuto.Arrancar()
autoVictor.Arrancar()

miAuto.Moverse(50)
autoVictor.Moverse(50)

miAuto.MostrarCantidadCombustible()
