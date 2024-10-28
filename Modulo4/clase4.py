"""
TRABAJANDO CON FECHA Y HORA
Libreria datetime
"""
import datetime

# Podemos ver la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print(fecha_hora_actual)

# Podemos dar el formato que queramos a la fecha
fecha_hora_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_hora_formateada)

# Podemos crear una fecha personalizada
# Los parametros en orden de : año, mes, dia, hora, minutos, segundos
fecha_hora_personalizada = datetime.datetime(1995, 9, 17, 9, 30, 27)
print(fecha_hora_personalizada.strftime("%d/%m/%Y %H:%M:%S"))

# Podemos hacer calculos con fechas con timedelta
today = datetime.date.today()
sumar_dias = today + datetime.timedelta(days=2)
print(f"Hoy es {today} y dentro de 2 dias es {sumar_dias}")

# Podemos convertir un string a fecha
fecha_string = "22-11-1996 8:05:12"
fecha_objeto = datetime.datetime.strptime(fecha_string, "%d-%m-%Y %H:%M:%S")
print(fecha_objeto)


"""
Libreria pytz: Para ver la hora y fecha de cualquier parte del mundo
Buscar documentacion de pytz
"""