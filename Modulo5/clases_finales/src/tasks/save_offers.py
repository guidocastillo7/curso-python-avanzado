import csv
from pathlib import Path
from prefect import task
# Python Decouple: sirve para trabajar con variables de entorno
from decouple import config

# IMPORTANTE INVESTIGAR EL USO DE PYTHON_PATH
FILE_PATH = Path(config("PYTHON_PATH") + "/files/offers.csv")


#@task(name="GUARDAR OFERTAS LABORALES EN CSV")
def save_offers(list_offers):
    with open(FILE_PATH, "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["puesto", "ubicacion", "url"]
        )

        writer.writerows(list_offers)