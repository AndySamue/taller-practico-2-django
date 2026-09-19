# Diagrama entidad-relación

```
+----------------------+          +----------------------------+
|     PokemonType      |          |          Pokemon            |
+----------------------+          +----------------------------+
| id (PK)              |    M    N| id (PK)                     |
| name                 |----------| name                        |
+----------------------+          | image                       |
                                   | height                      |
                                   | weight                      |
                                   | base_experience              |
                                   +----------------------------+
```

- Relación **muchos a muchos**: un `Pokemon` puede tener uno o dos `PokemonType`
  (ej. fire/flying), y un mismo `PokemonType` agrupa a muchos `Pokemon`. Django crea
  automáticamente la tabla intermedia para esta relación (`pokemons_pokemon_types`).

Este diagrama se puede pegar como imagen en el informe (captura de este archivo o
recreado en una herramienta como draw.io / dbdiagram.io).
