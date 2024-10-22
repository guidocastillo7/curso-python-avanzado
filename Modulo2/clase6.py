# EJERCICIO DE COMPRESOR DE IMAGENES

from PIL import Image
import os

def image_compressor(images_folder):
    try:
        # listdir para ver todos los archivos de la carpeta que pasamos por parametro
        for file in os.listdir(images_folder):

            # Con path.splitext lo que hacemos es separar el nombre del archivo y la extension
            # Devuelve esos dos valores separados, por eso ponemos dos variables
            file_name, file_extension = os.path.splitext(file)

            if file_extension == ".jpg" or file_extension == ".JPEG":
                print(f"Comprimiendo.. {file_name}{file_extension}")

                file_compress = Image.open(f"{images_folder}\{file}")
                # Cuando guardamos la imagen se juega con la quality para comprimirla
                file_compress.save(
                    f"{images_folder}\{file_name}_compressed{file_extension}",
                    optimize=True,
                    quality=70
                )

    except Exception as e:
        print(e)


if __name__ == '__main__':
    image_compressor("C:/Users/guido/Documents/PROGRAMACION/Curso Python Avanzado/Modulo2/imagenes")