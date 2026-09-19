from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from .forms import PokemonForm

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, "pokemons/pokemon_list.html", {"pokemons": pokemons})

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemons/pokemon_detail.html", {"pokemon": pokemon})

def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm()

    return render(request, "pokemons/pokemon_form.html", {"form": form})

def pokemon_update(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, "pokemons/pokemon_form.html", {"form": form})

def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    pokemon.delete()
    return redirect("pokemon_list")
