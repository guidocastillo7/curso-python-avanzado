"""
PROGRAMA PARA GUARDAR DATOS DE MI PC

Platform: Sirve para obtener datos detallados del sistema operativo,
procesador, etc..

Socket: Sirve para crear conexiones de red, servidores, etc..
en este caso la uso para ver la info del hostname y el ip
"""

import platform, socket


def save_pc_info():
    pc_data = "----------PC INFO----------\n"
    pc_data += "SISTEMA OPERATIVO: " + platform.system() \
            + " " + platform.version() + "\n"
    pc_data += "ARQUITECTURA: " + platform.machine() + "\n"
    pc_data += "PROCESADOR: " + platform.processor() + "\n"
    pc_data += "HOSTNAME: " + socket.gethostname() + "\n"
    pc_data += "IP: " + socket.gethostbyname(socket.gethostname())

    # Funcion Open: Sirve para abrir archivos, leer y editarlos
    pc_file = open("pc.txt", "w")
    # Aqui usamos el metodo write para editar el archivo
    pc_file.write(pc_data)
    # Siempre se debe cerrar el archivo despues de abrirlo
    pc_file.close()

    print("Guardado con exito!")


def read_pc_info():
    # Siempre es buena practica usar try y except para manejo de errores
    try:
        pc_file = open("pcc.txt", "r")
        # Aqui usamos el metodo read para leer el archivo
        pc_data = pc_file.read()

        print(pc_data)
        
        pc_file.close()
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    save_pc_info()
    read_pc_info()