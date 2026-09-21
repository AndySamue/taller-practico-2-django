from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Pokemon
from .forms import PokemonForm

# Vistas públicas

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, "pokemons/pokemon_list.html", {"pokemons": pokemons})


def pokemon_detail(request, id):  # Cambiado a 'id' para coincidir con la URL
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemons/pokemon_detail.html", {"pokemon": pokemon})


# Vistas protegidas (Fase 2)

@login_required
def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save()
            messages.success(request, f"¡Pokémon '{pokemon.name}' creado con éxito!")
            return redirect("pokemon_list")
    else:
        form = PokemonForm()
    
    return render(request, "pokemons/pokemon_form.html", {"form": form})


@login_required
def pokemon_update(request, id):  # Cambiado a 'id'
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save()
            messages.success(request, f"¡Pokémon '{pokemon.name}' actualizado con éxito!")
            return redirect("pokemon_list")
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, "pokemons/pokemon_form.html", {"form": form})


@login_required
@require_POST
def pokemon_delete(request, id):  # Cambiado a 'id'
    pokemon = get_object_or_404(Pokemon, id=id)
    nombre = pokemon.name
    pokemon.delete()
    messages.success(request, f"¡Pokémon '{nombre}' eliminado con éxito!")
    return redirect("pokemon_list")