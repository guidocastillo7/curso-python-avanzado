"""
CREANDO PAQUETES Y MODULOS

La carpeta 'geometria' seria un Paquete
Hay que crearle el archivo __init__.py para que python
lo identifique como un paquete.

Los archivos 'areas.py' y 'perimetros.py' serian los Modulos
que tienen que ir dentro del paquete geometria

Cuando se ejecuta el programa y esta usando los paquetes y modulos
se crea una carpeta '__pycache__' con unos archivos binarios
Esto es como una precompilacion del programa.
"""

from geometria import areas

# Cuando queremos importar varios metodos de un modulo
# Se hace de esta manera entre () para respetar los estandares de codigo Python
from geometria.perimetros import (
    perimetro_cuadrado,
    perimetro_circulo,
    perimetro_rectangulo
)


if __name__ == "__main__":

    lado_area = 5
    area_cuadrado = areas.area_cuadrado(lado_area)
    print(f"Area del cuadrado con lado de {lado_area}cm: {area_cuadrado}")

    lado_perimetro = 5
    perimetro_cdrd = perimetro_cuadrado(lado_perimetro)
    print(f"Perimetro del cuadrado con lado de {lado_perimetro}cm: {perimetro_cdrd}")

    radio_perimetro = 8
    perimetro_crcl = perimetro_circulo(radio_perimetro)
    print(f"Perimetro del circulo con radio de {radio_perimetro}cm: {perimetro_crcl}")

    base_perimetro = 20
    altura_perimetro = 10
    perimetro_rctngl = perimetro_rectangulo(base_perimetro, altura_perimetro)
    print(f"Perimetro del rectangulo con base de {base_perimetro}cm y altura de {altura_perimetro}cm: {perimetro_rctngl}")
