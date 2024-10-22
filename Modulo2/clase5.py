# TRABAJANDO CON IMAGENES, LIBRERIA PILLOW
# Importante leer la documentacion para saber el funcionamiento
# https://pypi.org/project/pillow/

from PIL import Image
# Para trabajar con las fuentes
from PIL import ImageFont
# Para dibujar las imagenes
from PIL import ImageDraw


def get_image(image_path):
    try:
        # Podemos abrir una imagen y ver sus propiedades
        image = Image.open(image_path)
        print(image.size)
        print(image.mode)
        print(image.format)

        # Podemos abrir la imagen
        image.show()

        # Podemos convertir la imagen a blanco y negro
        image_black_white = image.convert("L")
        image_black_white.show()
        # Podemos guardar la imagen editada
        image_black_white.save("dimitrescu_b&w.jpg")

        # Configuramos la fuente
        font = ImageFont.truetype("Roboto_Condensed/static/RobotoCondensed-Black.ttf", 150)
        # Configuramos la imagen a dibujar
        draw = ImageDraw.Draw(image)
        # Y configuramos lo que queremos escribirle
        draw.text(
            (250, 0),
            "Resident Evil VIII",
            (255, 255, 255),
            font
        )

        image.show()
        image.save("dimitrescu_draw.jpg")

        """Podemos crear un Thumbnai, que sirve para reducir
        la imagen en tamaño y peso"""
        image.thumbnail((960, 540))
        image.show()
        image.save("dimitrescu_thumbnail.jpg")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_image("Dimitrescu.jpg")