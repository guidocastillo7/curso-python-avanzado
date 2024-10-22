# TRABAJANDO CON ARCHIVOS CSV
import csv
from pathlib import Path

FILE_PATH = Path("users.csv")


def read_csv():
    try:
        with open(FILE_PATH, "r") as file:
            # DictReader sirve para convertir los datos del csv en diccionario
            reader = csv.DictReader(file)

            for row in reader:
                print(row.get("first_name"), ":" , row.get("email"))

    except Exception as e:
        print(e)


def write_csv():
    try:
        """Aqui lo abrimos con permisos de 'a', que significa
        append, para agregar datos, en cambio con permisos de 'w'
        borraria todo y escribiria desde 0"""
        with open(FILE_PATH, "a") as file:

            # DictWriter sirve para escribir datos en el csv
            writer = csv.DictWriter(
                # Se deben pasar los nombres de los campos del archivo en forma de lista
                file, fieldnames=["first_name", "last_name", "email"]
            )

            # writerows sirve para escribir los datos en el csv
            # pasandolos en una lista de diccionarios con los datos
            # deben estar ordenados los campos en orden
            writer.writerows([
                {
                    "first_name":"Guido",
                    "last_name":"Castillo",
                    "email":"guido@gmail.com"
                },
                {
                    "first_name":"Adolfo",
                    "last_name":"Castillo",
                    "email":"adolfo@gmail.com"
                }
            ])
            print("Datos agregados correctamente")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    write_csv()
    read_csv()