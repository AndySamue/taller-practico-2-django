from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField(blank=True)
    height = models.PositiveIntegerField(help_text="Altura en decimetros (segun la PokeAPI)")
    weight = models.PositiveIntegerField(help_text="Peso en hectogramos (segun la PokeAPI)")
    base_experience = models.PositiveIntegerField(null=True, blank=True)
    types = models.ManyToManyField(PokemonType, related_name="pokemons", blank=True)
    abilities = models.JSONField(default=list, blank=True, help_text="Lista de {name, is_hidden} segun la PokeAPI")
    hp = models.PositiveIntegerField(null=True, blank=True)
    attack = models.PositiveIntegerField(null=True, blank=True)
    defense = models.PositiveIntegerField(null=True, blank=True)
    special_attack = models.PositiveIntegerField(null=True, blank=True)
    special_defense = models.PositiveIntegerField(null=True, blank=True)
    speed = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
