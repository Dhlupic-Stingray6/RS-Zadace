import re
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator

class Actor(BaseModel):
    name: str
    surname: str

class Writer(BaseModel):
    name: str
    surname: str

class Film(BaseModel):
    Title: str
    Year: int
    Rated: str
    Runtime: Optional[int]  
    Genre: List[str]
    Language: str
    Country: str
    Actors: List[str]
    Plot: str
    Writer: str
    Awards: Optional[str] = "No awards information"
    Poster: Optional[str] = None
    imdbID: str
    imdbRating: Optional[float] = None     
    imdbVotes: Optional[str] = None  
    totalSeasons: Optional[int] = None
    ComingSoon: Optional[bool] = False
    Images: Optional[List[str]] = Field(default_factory=list)

   

  
    @field_validator("Year", mode="before", check_fields=False)
    @classmethod
    def parse_year(cls, value):
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            match = re.search(r"(\d{4})", value)
            if match:
                return int(match.group(1))
            else:
                raise ValueError("Godina mora imati barem jedan broj sa 4 znamenke")
        raise ValueError("Godina mora biti integer ili string koji sadrži 4 znamenke")

   
    @field_validator("Runtime", mode="before", check_fields=False)
    @classmethod
    def parse_runtime(cls, value):
        if value is None:
            return value
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            if value.strip().upper() == "N/A":
                return None
            digits = re.search(r"(\d+)", value)
            if digits:
                return int(digits.group(1))
            else:
                raise ValueError("Runtime mora sadržavati broj")
        raise ValueError("Runtime mora biti integer ili string koji sadrži broj")
    
   
    @field_validator("imdbRating", mode="before", check_fields=False)
    @classmethod
    def parse_imdb_rating(cls, value):
        if value is None:
            return value
        if isinstance(value, (float, int)):
            return float(value)
        if isinstance(value, str):
            if value.strip().upper() == "N/A":
                return None
            try:
                return float(value)
            except ValueError:
                raise ValueError("imdbRating must be a number between 0 and 10")
        return value

   
    @field_validator("Genre", mode="before", check_fields=False)
    @classmethod
    def parse_genre(cls, value):
        if isinstance(value, str):
            return [s.strip() for s in value.split(",")]
        return value

    
    @field_validator("Actors", mode="before", check_fields=False)
    @classmethod
    def parse_actors(cls, value):
        if isinstance(value, str):
            return [s.strip() for s in value.split(",")]
        return value

   

    @field_validator("Year")
    @classmethod
    def check_year(cls, value: int) -> int:
        if value <= 1900:
            raise ValueError("Godina mora biti veća od 1900")
        return value

    @field_validator("Runtime")
    @classmethod
    def check_runtime(cls, value: Optional[int]) -> Optional[int]:
       
        if value is None:
            return value
        if value <= 0:
            raise ValueError("Runtime mora biti veći od 0")
        return value

    @field_validator("imdbRating")
    @classmethod
    def check_imdb_rating(cls, value: Optional[float]) -> Optional[float]:
        if value is None:
            return value
        if value < 0 or value > 10:
            raise ValueError("imdbRating must be between 0 and 10")
        return value

    @field_validator("Images", mode="before", check_fields=False)
    @classmethod
    def check_images(cls, value: Optional[List]) -> List[str]:
        if value is None:
            return []
        if not isinstance(value, list):
            raise ValueError("Slike moraju biti liste stringova")
        if not all(isinstance(item, str) for item in value):
            raise ValueError("Svi itemi u Images trebaju biti stringovi")
        return value
