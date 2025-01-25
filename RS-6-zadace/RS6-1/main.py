from fastapi import FastAPI
from models import Film, CreateFilm

app = FastAPI()

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]



@app.get('/filmovi', response_model=list[Film])
def dohvati_filmove(genre = None, min_godina : int = 2000):
    pronadeni_filmovi = [film for film in filmovi if(genre is None) and (film['godina'] >= min_godina)]
    return pronadeni_filmovi


@app.get('/filmovi/{id}', response_model=Film)
def dohvati_filmove(id: int):
    pronaden_film = next((film for film in filmovi if film['id'] == id), None)
    return pronaden_film


@app.post('/filmovi', response_model=Film)
def add_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    film_s_id : Film = {"id": new_id, **film.model_dump()}
    filmovi.append(film_s_id)
    return film_s_id