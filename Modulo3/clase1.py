"""
TRABAJANDO CON CADENAS DE TEXTO
Slicing: Seria como cortar la cadena o tomar algun caracter
"""

cadena = "Curso Python Avanzado"
# Aqui tomo un caracter por su indice
print(cadena[2])
# Si lo pongo asi en negativo me toma el ultimo caracter
print(cadena[-1])
# Puede elegir de donde a donde cortar
print(cadena[4:8])

"""
Cuando ponemos 3 indices significa lo siguiente:
El primero es donde empieza
El segudon es donde termina
El tercero significa cada cuantos indices quieres contar
"""
# Por ejemplo queremos contar de 2 en 2
print(cadena[0:8:2])
# De 3 en 3
print(cadena[0:10:3])
# Poniendo solo los dos puntos toma toda la cadena
print(cadena[:])

# Y podemos contar de atras para alante poniendo -1 en el tercer indice
print(cadena[::-1])

"""
Podemos convertir una cadena de varias palabra a una lista
Split: Se pasa por parametro el caracter que quieres q separe cada elemento de la lista
"""
# Ejemplo usamos el espacio para separar cada elemento en la lista
lenguajes = "Python JavaScript Go C++ Java"
lista_lenguajes = lenguajes.split(" ")
print(lista_lenguajes)

# Y podemos usar el mismo funcionamiento de los indices para las listas
print(lista_lenguajes[1:3])
print(lista_lenguajes[0:5:2])
print(lista_lenguajes[::-1])


"""
Podemos tomar una parte especifica de una cadena
Por ejemplo queremos tomar el dominio de un emmail
O podemos tomar solo el usuario del email
"""
email = "guido@gmail.com"
# Aqui buscamos el indice especifico del arroba
# Le sumo 1 para empezar desde ahi y lo recorro hasta el final
dominio = email[email.index("@") + 1:]
print(dominio)
# Para el usuario ponemos el indice del arroba donde queremos que termine de recorrer
usuario = email[:email.index("@")]
print(usuario)