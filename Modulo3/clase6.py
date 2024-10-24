"""
Ejercicio de palindromo
"""

"""def is_palindromo(text):
    text_normal = text.replace(" ", "")
    text_reverse = text[::-1].replace(" ", "")

    if text_reverse == text_normal:
        print(f"{text} Si es un palindromo!")
    else:
        print(f"{text} No es un palindromo!")


texto = input("Escribe una palabra o frase: ")
is_palindromo(texto)"""


"""
Ejercicio de lista al reverso
Dada una lista de strings, escribe una funcio que imprima cada str al reves
"""

# Esta es una manera de hacerla basica
def revert_list(lista):
    final_list = []

    for str in lista:
        final_list.append(str[::-1])
    
    return final_list

# Esta es una manera de hacerla avanzada
def revert_list_pro(lista):

    # A esto se le llama List Comprehension
    final_list = [str[::-1] for str in lista]

    return final_list


lista_normal = ["Hola mundo", "Hola Python", "1 2 3 4 5 6 7 8"]
reversed_list = revert_list(lista_normal)
print(reversed_list)

reversed_list_pro = revert_list_pro(lista_normal)
print(reversed_list_pro)