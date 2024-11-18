import requests
from jinja2 import Template
import json


# Получаем данные о первых 20 покемонах
def get_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon?limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        pokemons_list = response.json()["results"]
        pokemons_data = []

        for pokemon in pokemons_list:
            # Получаем детальную информацию о каждом покемоне
            detail_response = requests.get(pokemon["url"])
            if detail_response.status_code == 200:
                detail_data = detail_response.json()
                pokemon_info = {
                    "name": detail_data["name"],
                    "height": detail_data["height"],
                    "weight": detail_data["weight"],
                    "image": detail_data["sprites"]["front_default"],
                    "types": [t["type"]["name"] for t in detail_data["types"]],
                }
                pokemons_data.append(pokemon_info)

        return pokemons_data
    return None


# HTML шаблон с использованием Jinja2
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Pokemon List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }
        .pokemon-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .pokemon-card {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .pokemon-card img {
            width: 120px;
            height: 120px;
        }
        .pokemon-card h2 {
            margin: 10px 0;
            text-transform: capitalize;
            color: #333;
        }
        .type-tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 2px;
            border-radius: 15px;
            background-color: #4CAF50;
            color: white;
            font-size: 0.8em;
        }
    </style>
</head>
<body>
    <h1>Pokemon List</h1>
    <div class="pokemon-grid">
    {% for pokemon in pokemons %}
        <div class="pokemon-card">
            <img src="{{ pokemon.image }}" alt="{{ pokemon.name }}">
            <h2>{{ pokemon.name }}</h2>
            <p>Height: {{ pokemon.height/10 }}m</p>
            <p>Weight: {{ pokemon.weight/10 }}kg</p>
            <div>
                {% for type in pokemon.types %}
                    <span class="type-tag">{{ type }}</span>
                {% endfor %}
            </div>
        </div>
    {% endfor %}
    </div>
</body>
</html>
"""

# Получаем данные
pokemon_data = get_pokemon_data()

# Создаем HTML файл
if pokemon_data:
    # Создаем шаблон
    template = Template(html_template)

    # Рендерим HTML
    html_content = template.render(pokemons=pokemon_data)

    # Сохраняем в файл
    with open("pokemon_list.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML файл успешно создан!")
else:
    print("Ошибка при получении данных")
