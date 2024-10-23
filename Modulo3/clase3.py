"""
Funciones para busqueda y reemplazo de cadenas de texto
"""

text = """Venezuela, oficialmente República Bolivariana de Venezuela, es un país
soberano situado en la parte septentrional de América del Sur y el Caribe,
constituido por un área continental y por un gran número de islas e islotes en el mar Caribe,
cuya capital y mayor aglomeración urbana es la ciudad de Caracas.
El territorio conocido actualmente como Venezuela fue colonizado por España en 1522,
en medio de la resistencia de los pueblos indígenas que habitaban la región."""

palabra_buscar = input("Que palabra quieres buscar?: ")
# El metodo find me devuelve el indice donde esta la palabra
# Solo me devuelve el primer encontrado
index = text.find(palabra_buscar)
if index == -1:
    print(f"La palabra '{palabra_buscar}' no fue encontrada.")
else:
    print(f"La palabra '{palabra_buscar}' se encuentra en el indice '{index}'")


# El metodo count me dice cuantas veces esta esa palabra
total_encontrada = text.count(palabra_buscar)
print(f"La palabra '{palabra_buscar}' se encuentra '{total_encontrada}' veces")


# El metodo replace me sirve para cambiar una palabra a otra deseada
# 2 parametros: el primero la palabra que quiero cambiar
# el segundo la palabra que quiero añadir
texto_cambiado = text.replace("Venezuela", "Venekia")
print("\n", texto_cambiado, "\n")

# El tercer parametro sirve para especificar cuantas veces quiero cambiar la palabra
# en caso de que se repita mas de una vez
texto_cambiado2 = text.replace("Venezuela", "Venekia", 1)
print(texto_cambiado2)