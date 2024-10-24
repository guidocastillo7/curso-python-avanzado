"""
EXPRESIONES REGULARES
"""

import re

cadena = "Vamos a aprender expresiones regulares con python"
# Aqui podemos buscar la palabra pasada en el parametro, en la cadena pasada al parametro
# Nos devuelve un objeto de la busqueda
busqueda = re.search("aprender", cadena)
print(busqueda)

# Podemos escribir un patron de busqueda para algo especifico
# Por ejemplo aqui buscamos fechas en un texto
texto = "La fecha de vencimiento es 2024-12-31 y la fecha de inicio fue 2023-10-20"
# Aqui creamos el patron requerido
# El \d significa que va a ser un numero, puede ser decimal tambien
# Y lo que va entre llaves dice cuantos numeros tienen que ser
patron_fecha = r"\d{4}-\d{2}-\d{2}"
# El metodo findall me busca todas las coincidencias en el texto
# Y me los devuelve en una lista
fechas_encontradas = re.findall(patron_fecha, texto)
print(fechas_encontradas)


# Podemos hacer un reemplazo de texto basado en patrones
text = "El numero de telefono es 39-652-4875"
patron_numero = r"\d{2}-\d{3}-\d{4}"
# Con el metodo sub reemplazo el texto por el que paso al parametro
new_text = re.sub(patron_numero, "#######", text)
print(new_text)


# Ejemplo de extraccion de url de un html
html = "<p>Enlace <a href='https://www.google.com'>Ir a google</a>"
# (.*?) quiere decir que me tome todo lo que hay en esa parte del texto
patron_url = r"<a href='(.*?)'>(.*?)</a>"
urls = re.findall(patron_url, html)
print(urls)

# O los puedo imprimir mas ordenado
for url in urls:
    enlace, texto = url
    print(f"URL: {enlace}, TEXTO: {texto}")