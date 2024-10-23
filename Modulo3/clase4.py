"""
FORMATEO DE CADENAS
Con la funcion format le pasamos por parametros los valores
que quedan en las llaves, por orden de posicion
"""

name = "Guido"
age = 20
print("Hola soy {} y tengo {} años".format(name, age))

# Puedo hacer tambien un calculo en los parametros
print("Soy {} y tengo {} años".format(name, age + 10))

# Sirve para cuando queremos hacer una sentencia SQL
sql_insert = "insert into users(name, age) values ('{}', '{}')".format(name, age)
print(sql_insert)

# Tambien se puede ordenar con los indices de los parametros
print("Tengo {1} años, me llamo {0}".format(name, age))

# Tambien podemos poner nombres a los parametros personalizados
print("Sono {nome} ho {eta} anni".format(nome=name, eta=age))

# Podemos convertir a float los numeros
# Escribiendo :.2f
product = "Iphone 14"
price = 500
print("El {} tiene un precio de {:.2f}$".format(product, price))

# Hay otras funciones para formatear numeros
num = 12400.56784
# Si tienen muchos decimales y quieres menos
print("{:.3f}".format(num))
# Si se quieren distinguir con la coma los miles
print("{:,}".format(num))
# Si se quiere formatear a notacion cientifica
print("{:e}".format(num))

# Puedo poner una cantidad de espacios antes del dato
numero = 40
print("El numero es:{:>5}".format(numero))
# Y podemos rellenar el numero con ceros a la derecha e izquierda con < y >
print("El numero: {:0>5}".format(numero))


# Una manera de formatear la fecha
from datetime import datetime
date = datetime.now()
print("Fecha {:%d/%m/%Y %H:%M:%S}".format(date))