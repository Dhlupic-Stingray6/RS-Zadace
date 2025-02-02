import json
from pathlib import Path
from models import Film
from typing import List

def load_films() -> List[Film]:
    file_path = Path('films.json')
    with file_path.open(encoding="utf-8") as f:
        films_data = json.load(f)
    films = [Film(**film) for film in films_data]
    return films

film_list = load_films()


#Definiramo put do JSON datoteke
#učitavamo podatke 
#kreiramo listu instanci sa list comprehension sintaksom i ** operatorom
#lista filmova koju možemo koristiti u aplikaciji