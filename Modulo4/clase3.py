"""
GENERANDO VALORES ALEATORIOS
Libreria Random
"""

import random

# Aqui generamos un numero entero aleatorio del 1 al 20
random_number = random.randint(1, 20)
print(random_number)

list_numbers = []
for i in range(20):
    random_number = random.randint(1, 20)
    list_numbers.append(random_number)
print(list_numbers)


# Aqui generamos un numero float aleatorio del 0 al 1
random_float = random.random()
print(random_float)
list_floats = [random.random() for i in range(10)]
print(list_floats)


"""
Libreria secrects: Para generar token aleatorio en bytes
"""
import secrets
random_secret = secrets.token_bytes(4)
print(random_secret)


"""
Libreria uuid: Para generar un id alfanumerico unico aleatorio
"""
import uuid
random_id = uuid.uuid4()
print(random_id)