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

TYPE_COLORS = {
    "normal": "#A8A77A", "fire": "#EE8130", "water": "#6390F0",
    "electric": "#F7D02C", "grass": "#7AC74C", "ice": "#96D9D6",
    "fighting": "#C22E28", "poison": "#A33EA1", "ground": "#E2BF65",
    "flying": "#A98FF3", "psychic": "#F95587", "bug": "#A6B91A",
    "rock": "#B6A136", "ghost": "#735797", "dragon": "#6F35FC",
    "dark": "#705746", "steel": "#B7B7CE", "fairy": "#D685AD",
}

STAT_FIELDS = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]

STAT_LABELS_ES = {
    "hp": "HP", "attack": "Ataque", "defense": "Defensa",
    "special_attack": "At. Especial", "special_defense": "Def. Especial", "speed": "Velocidad",
}

STAT_COLORS = {
    "hp": "#F95D5D", "attack": "#F5A25D", "defense": "#F7D358",
    "special_attack": "#6EB5F0", "special_defense": "#7FDB8E", "speed": "#F76FB0",
}

STAT_SCALE_MAX = 180


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
def type_color(type_name):
    return TYPE_COLORS.get((type_name or "").lower(), "#A8A77A")


@register.filter
def dex_number(pokemon_id):
    try:
        return f"{int(pokemon_id):03d}"
    except (TypeError, ValueError):
        return pokemon_id


@register.filter
def pokemon_stats(pokemon):
    rows = []
    for field in STAT_FIELDS:
        value = getattr(pokemon, field, None)
        if value is None:
            continue
        rows.append({
            "label": STAT_LABELS_ES[field],
            "value": value,
            "pct": min(100, round(value * 100 / STAT_SCALE_MAX)),
            "color": STAT_COLORS[field],
        })
    return rows


@register.filter
def pokemon_stats_total(pokemon):
    return sum(getattr(pokemon, field, None) or 0 for field in STAT_FIELDS)
