"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
Platform: Sirve para obtener datos detallados del sistema operativo, procesador, etc..
Socket: Sirve para crear conexiones de red, servidores, etc..
en este caso la uso para ver la info del hostname y el ip
"""

import platform, socket
# Libreria Path: Sirve en este caso para entrar a una ruta especifica
from pathlib import Path

# De buena practica las constantes se crean con mayusculas
FILE_PATH = Path("pc.txt")


def save_pc_info():
    pc_data = "----------PC INFO----------\n"
    pc_data += "SISTEMA OPERATIVO: " + platform.system() \
            + " " + platform.version() + "\n"
    pc_data += "ARQUITECTURA: " + platform.machine() + "\n"
    pc_data += "PROCESADOR: " + platform.processor() + "\n"
    pc_data += "HOSTNAME: " + socket.gethostname() + "\n"
    pc_data += "IP: " + socket.gethostbyname(socket.gethostname())

    """Bloque with: Sirve en este caso para no tener que estar abriendo y
    cerrando los archivos, porque automaticamente al salir del bloque with
    se cierra el archivo"""
    with open(FILE_PATH, "w") as pc_file:
        pc_file.write(pc_data)

    print("Guardado con exito!")


def read_pc_info():
    try:
        with open(FILE_PATH, "r") as pc_file:
            pc_data = pc_file.read()
            print(pc_data)
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    save_pc_info()
    read_pc_info()