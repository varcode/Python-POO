
def obtenerEdad(fecha):
    edad = 20210918 - fecha
    return edad//10000


nombre = 'Gustavo'
fecha_de_nacimiento = '01-11-1989'
fecha_de_nacimiento_formato_aaaammdd = (int(fecha_de_nacimiento[6:]) * 10000 
                                       + int(fecha_de_nacimiento[3:5]) * 100 
                                       + int(fecha_de_nacimiento[1:2]))

edad = obtenerEdad(fecha_de_nacimiento_formato_aaaammdd)



print('El usuario ' + nombre + ' tiene ' + str(edad) + ' años ')


