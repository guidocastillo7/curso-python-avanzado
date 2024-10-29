"""
EJERCICIO DE SERIE FIBONACCI
"""

def fibonacci(num):

    lista_fibonacci = [0, 1]

    while len(lista_fibonacci) < num:
        suma_nums = lista_fibonacci[-1] + lista_fibonacci[-2]
        lista_fibonacci.append(suma_nums)
    
    return lista_fibonacci

lista_fibonacci = fibonacci(10)
print(lista_fibonacci)



"""
EJERCICIO PARA SABER QUE DIA DE SEMANA NACISTE
"""
import datetime

def dia_nacimiento(fecha_nacimiento):
    semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    fecha = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    indice_dia = fecha.weekday()
    dia = semana[indice_dia]

    return dia

dia = dia_nacimiento("17-9-1995")
print(f"Naciste un dia {dia}")