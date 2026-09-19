# Taller Práctico 2 — Pokedex (Django, MVT)

Aplicación web con arquitectura MVT para la gestión de Pokemon, usando el ORM de
Django y una base de datos relacional (SQLite en desarrollo). Los datos se pueden
poblar automáticamente desde la [PokeAPI](https://pokeapi.co/docs/v2). Incluye CRUD
completo de Pokemon mediante formularios.

## Modelo de datos

- **PokemonType**: `name` (ej. fire, water, grass).
- **Pokemon**: `name`, `image` (sprite), `height`, `weight`, `base_experience`,
  `types` (ManyToMany a `PokemonType`, ya que un Pokemon puede tener uno o dos tipos).

## Requisitos

- Python 3.10+
- pip

## Instalación (Windows / PowerShell)

```powershell
# 1. Clonar el repositorio y entrar a la carpeta
git clone <URL_DEL_REPOSITORIO>
cd TallerPractico2

# 2. Crear y activar el entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Copiar el archivo de variables de entorno y generar tu propia SECRET_KEY
copy .env.example .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Pegar el valor generado en SECRET_KEY dentro de .env

# 5. Aplicar migraciones
python manage.py migrate

# 6. (Opcional) Crear un superusuario para entrar al panel de administración
python manage.py createsuperuser

# 7. Levantar el servidor de desarrollo
python manage.py runserver
```

La aplicación queda disponible en http://127.0.0.1:8000/

## Cargar datos de ejemplo desde la PokeAPI (opcional)

El proyecto incluye un servicio que trae Pokemon reales desde
`https://pokeapi.co/api/v2/pokemon/` y crea automáticamente los tipos asociados:

```powershell
python manage.py shell -c "from pokemons.services.pokemon_service import load_pokemons; print(load_pokemons(limit=20))"
```

`limit` controla cuántos Pokemon se cargan (por defecto 20).

## Variables de entorno

Ver `.env.example`. Nunca se debe subir el archivo `.env` real al repositorio (ya
está excluido en `.gitignore`); cada integrante genera su propia `SECRET_KEY` local.

| Variable       | Descripción                                   | Valor por defecto        |
|----------------|------------------------------------------------|---------------------------|
| `SECRET_KEY`   | Clave secreta de Django (obligatoria)          | —                         |
| `DEBUG`        | Modo debug                                     | `False`                  |
| `ALLOWED_HOSTS`| Hosts permitidos, separados por coma           | `localhost,127.0.0.1`    |

## Estado del proyecto

- [x] Fase 1 — Modelos, base de datos y configuración de entorno
- [ ] Fase 2 — Vistas CRUD y seguridad de backend (autenticación, validaciones)
- [ ] Fase 3 — Formularios, templates y experiencia de usuario
- [ ] Fase 4 — Integración, pruebas, informe y entrega
