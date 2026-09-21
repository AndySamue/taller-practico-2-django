from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Pokemon
from .forms import PokemonForm

POKEMONS_PER_PAGE = 12


def pokemon_list(request):
    pokemon_qs = Pokemon.objects.all().order_by("name")
    paginator = Paginator(pokemon_qs, POKEMONS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "pokemons/pokemon_list.html", {"page_obj": page_obj})


def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemons/pokemon_detail.html", {"pokemon": pokemon})


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
def pokemon_update(request, id):
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
def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        nombre = pokemon.name
        pokemon.delete()
        messages.success(request, f"¡Pokémon '{nombre}' eliminado con éxito!")
        return redirect("pokemon_list")
    return render(request, "pokemons/pokemon_confirm_delete.html", {"pokemon": pokemon})
