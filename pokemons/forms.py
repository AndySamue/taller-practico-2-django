from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"

    def clean_height(self):
        height = self.cleaned_data.get("height")
        if height is not None and height <= 0:
            raise forms.ValidationError("La altura debe ser mayor a 0.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get("weight")
        if weight is not None and weight <= 0:
            raise forms.ValidationError("El peso debe ser mayor a 0.")
        return weight