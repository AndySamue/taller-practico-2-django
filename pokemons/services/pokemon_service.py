import requests

from ..models import Pokemon, PokemonType

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_list(limit=20):
    response = requests.get(POKEAPI_BASE_URL, params={"limit": limit})
    if response.status_code != 200:
        print(f"Error al obtener el listado de pokemon: {response.status_code}")
        return []

    return response.json()["results"]


def get_pokemon_detail(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener el detalle del pokemon: {response.status_code}")
        return None

    return response.json()


def load_pokemons(limit=20):
    if Pokemon.objects.count():
        return f"ya existen {Pokemon.objects.count()} pokemon"

    for entry in get_pokemon_list(limit):
        detail = get_pokemon_detail(entry["url"])
        if not detail:
            continue

        pokemon = Pokemon.objects.create(
            name=detail["name"],
            image=detail["sprites"]["front_default"] or "",
            height=detail["height"],
            weight=detail["weight"],
            base_experience=detail.get("base_experience"),
        )
        for entry_type in detail["types"]:
            pokemon_type, _ = PokemonType.objects.get_or_create(name=entry_type["type"]["name"])
            pokemon.types.add(pokemon_type)

    return f"Se cargaron {Pokemon.objects.count()} pokemon"
