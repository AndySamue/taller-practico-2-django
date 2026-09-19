from django.contrib import admin

from .models import Pokemon, PokemonType


@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "height", "weight", "base_experience")
    list_filter = ("types",)
    search_fields = ("name",)
