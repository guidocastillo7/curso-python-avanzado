# TRABAJANDO CON ARCHIVOS JSON

import requests
import json
# Libreria webbrowser para abrir el navegador
import webbrowser

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_info(pokemon_name):
    url = BASE_URL + pokemon_name
    response = requests.get(url)

    try:
        pokemon_data = json.loads(response.text)
        pokemon_sprites = pokemon_data["sprites"]
        pokemon_image = pokemon_sprites["front_default"]

        webbrowser.open(pokemon_image)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    pokemon_name = input("Escribe el nombre del pokemon: ")
    get_pokemon_info(pokemon_name)