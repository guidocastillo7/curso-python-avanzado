# CONCATENACION DE CADENAS

# Esta es la concatenacion basica sumando dos str
cadena1 = "Hola, "
cadena2 = "como estas?" 
print(cadena1 + cadena2)

# No se puede concatenar un str con un int, habria q transformar el int a str
frase = "Mi edad es "
edad = 25
print(frase + str(edad))

# Concatenacion usando f-strings
nombre = "Guido"
apellido = "Castillo"
edad = "25"
print(f"Buenos dias, mi nombre es {nombre} {apellido} y tengo {edad} años")

# Podemos convertir una lista a string
lista = [1, 2, 3, 4, 5]
resultado = ""
for num in lista:
    resultado += str(num) + " "
print(resultado)

# Pero lo podemos hacer mejor con el metodo join
palabras = ["Hola", "mundo", "Python!"]
# Se crea el string con los valores de la lista separados por el valor que este antes del join
convertir = " ".join(palabras)
print(convertir)