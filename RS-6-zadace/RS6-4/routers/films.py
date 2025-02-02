from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import Film
from utils import film_loader


router = APIRouter(prefix="/filmovi")

filtered_films = film_loader.film_list

@router.get("/", response_model=List[Film])
def get_all_films(
    min_year: Optional[int] = Query(
        None, ge=1901, description="Godina mora biti veća od 1900"
    ),
    max_year: Optional[int] = Query(
        None, description="Godina max"
    ),
    min_rating: Optional[float] = Query(
        None, ge=0, le=10, description="Najmanji IMDb rating treba biti 0-10"
    ),
    max_rating: Optional[float] = Query(
        None, ge=0, le=10, description="Najveći IMDb rating treba biti 0-10"
    ), 
    film_type: Optional[str] = Query(
        None, regex="^(movie|series)$", description="Treba biti 'movie' ili 'series' "
    )
):
    

    if min_year is not None:
        filtered_films = [film for film in filtered_films if film.Year >= min_year]
    if max_year is not None:
        filtered_films = [film for film in filtered_films if film.Year <= max_year]   
    if min_rating is not None:
        filtered_films = [
            film for film in filtered_films
            if film.imdbRating is not None and film.imdbRating >= min_rating 
        ]
    if max_rating is not None:
        filtered_films = [
            film for film in filtered_films
            if film.imdbRating is not None and film.imdbRating <= max_rating 
        ]
    if film_type is not None:
        filtered_films = [film for film in filtered_films if film.type == film_type]

    return filtered_films


@router.get("/filmovi/imdb/{imdbID}", response_model=Film)
def get_film_by_imdb(imdbID: str):
    film = next((film for film in filtered_films if film.imdbID == imdbID), None)
    if film is None:
        raise HTTPException(
            status_code=404, detail=f"Film with IMDb ID '{imdbID}' not found."
        )
    return film

@router.get("/filmovi/title/{title}", response_model=Film)
def get_film_by_title(title: str):
    film = next(
        (film for film in filtered_films if film.Title.lower() == title.lower()), None
    )
    if film is None:
        raise HTTPException(
            status_code=404, detail=f"Film with title '{title}' not found."
        )
    return film