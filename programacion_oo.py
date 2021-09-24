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
    __marca_auto = ''

    def __init__(self, capacidad_combustible, marca):
       self.__capacidad_combustible_litros = capacidad_combustible
       self.__marca_auto = marca



    def __init__(self, capacidad_combustible):
        self.__capacidad_combustible_litros = capacidad_combustible
        self.__mensaje = 'Constructor capacidad combustible'

    def Arrancar(self):
        self.__km_recorridos_trayecto = 0

    def Detenerse(self):
        self.__km_recorridos_total = self.__km_recorridos_total + self.__km_recorridos_trayecto
    
    def Moverse(self, km_recorridos):
        self.__km_recorridos_trayecto = self.__km_recorridos_trayecto + km_recorridos

    def MostrarCantidadCombustible(self):
        print(self.__cantidad_combustible)

    def CargarNafta(self, Cantidad_Nafta_A_Cargar):
        self.__cantidad_combustible = self.__cantidad_combustible + Cantidad_Nafta_A_Cargar

    #Este metodo sirve para verificar si se puede o no cargar nafta mas alla de la capacidad
    #del tanque de combustible.
    #O sea... no podes cargar mas nafta de lo que puede almacenar el auto no?
    #Lo que hago es sumar la cantidad de combustible que quiero cargar, pero que todavia
    #no cargue al auto, mas lo que tiene en el tanque actualmente cargado y pregunto
    #si no supera la capacidad del tanque del auto.
    def SePuedeCargarNafta(self, Cantidad_Nafta_A_Cargar):
        #El if, se utiliza para compara valores de variables o de variables y valores fijos ( 3,4,10000)
        #Si es verdadero, se ejecuta lo que esta dentro del IF
        #De lo contrario se ejecuta lo que esta en el ELSE
        #No es obligatorio poner ELSE
        if ( Cantidad_Nafta_A_Cargar + self.__cantidad_combustible > self.__capacidad_combustible_litros):
            return False
        else:
            return True

#Array de objeto (creo que se puede hacer) vacio
arrayDeAuto = []
print(" 1 - Ingresar auto")
print(" 2 - Salir")
opcionSeleccionada = int(input("Ingrese opcion:"))


#El WHILE va a ejecutar el codigo, hasta que la condicion que se encuentra entre paretesis
#sea falsa
while (opcionSeleccionada < 2 ):
    marca_auto_nuevo = input("Ingrese marca de auto:")
    capacidad_combustible_auto_nuevo = int(input("Ingrese la capacidad de combustible del auto:"))
    autoNuevo = Auto(capacidad_combustible_auto_nuevo, marca_auto_nuevo)
    arrayDeAuto.append(autoNuevo)
    print(" 1 - Ingresar auto")
    print(" 2 - Salir")
    opcionSeleccionada = int(input("Ingrese opcion:"))


'''
Este codigo es viejo!!


miAuto = Auto(50)

autoVictor = Auto(30)

miAuto.Arrancar()
autoVictor.Arrancar()

miAuto.Moverse(50)
autoVictor.Moverse(50)

if(miAuto.SePuedeCargarNafta(20)):
    miAuto.CargarNafta(20)


miAuto.MostrarCantidadCombustible()
'''