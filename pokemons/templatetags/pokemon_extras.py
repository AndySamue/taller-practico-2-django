from django import template

register = template.Library()

TYPE_LABELS_ES = {
    "normal": "Normal", "fire": "Fuego", "water": "Agua",
    "electric": "Electrico", "grass": "Planta", "ice": "Hielo",
    "fighting": "Lucha", "poison": "Veneno", "ground": "Tierra",
    "flying": "Volador", "psychic": "Psiquico", "bug": "Bicho",
    "rock": "Roca", "ghost": "Fantasma", "dragon": "Dragon",
    "dark": "Siniestro", "steel": "Acero", "fairy": "Hada",
}

TYPE_ICONS = {
    "normal": "⚪", "fire": "🔥", "water": "💧", "electric": "⚡",
    "grass": "🌿", "ice": "❄️", "fighting": "🥊", "poison": "☠️",
    "ground": "⛰️", "flying": "🕊️", "psychic": "🔮", "bug": "🐛",
    "rock": "🪨", "ghost": "👻", "dragon": "🐉", "dark": "🌑",
    "steel": "⚙️", "fairy": "✨",
}

TYPE_SOFT_COLORS = {
    "normal": "#F2F1E8", "fire": "#FFE8DA", "water": "#E1EBFF",
    "electric": "#FFF6D6", "grass": "#E4F5DC", "ice": "#E4FBFA",
    "fighting": "#FBE0DE", "poison": "#F4E1F4", "ground": "#FBF3DD",
    "flying": "#EDE7FC", "psychic": "#FEE1EA", "bug": "#F1F5D6",
    "rock": "#F3EED9", "ghost": "#E9E3F0", "dragon": "#E5DBFE",
    "dark": "#E9E2DE", "steel": "#EDEDF3", "fairy": "#FBE7F1",
}


@register.filter
def type_label(type_name):
    return TYPE_LABELS_ES.get((type_name or "").lower(), (type_name or "").capitalize())


@register.filter
def type_icon(type_name):
    return TYPE_ICONS.get((type_name or "").lower(), "")


@register.filter
def type_soft_color(type_name):
    return TYPE_SOFT_COLORS.get((type_name or "").lower(), "#F2F1E8")


@register.filter
def dex_number(pokemon_id):
    try:
        return f"{int(pokemon_id):03d}"
    except (TypeError, ValueError):
        return pokemon_id
