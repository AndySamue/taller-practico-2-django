from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("pokedex/", pokemon_list, name="pokemon_list"),
    path("pokemons/<int:id>", pokemon_detail, name="pokemon_detail"),
    path("pokemon/create", pokemon_create, name="pokemon_create"),
    path("pokemons/update/<int:id>", pokemon_update, name="pokemon_update"),
    path("pokemons/delete/<int:id>", pokemon_delete, name="pokemon_delete"),
]