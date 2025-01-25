from pydantic import BaseModel
from typing import Optional, Literal, TypedDict
from datetime import datetime

class Izdavac(BaseModel):
    naziv : str
    adresa : str


class Knjiga(BaseModel):
    naslov: str
    autor_ime : str
    autor_prezime: str
    godinja_izdavanja: Optional[int] = datetime.now().year
    izdavac: Izdavac


class Admin(BaseModel):
    ime: str
    prezime:str
    email: str
    ovlasti: list[Literal['dodavanje', 'brisanje', 'ažuriranje', 'čitanje']]


class Stol_info(TypedDict):
    broj : int
    lokacija: Literal['terasa', 'prizemlje', 'kat' ]

class Jelo(BaseModel):
    id : int
    naziv : str
    cijena : float


class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info : Stol_info
    lista_jela : list[Jelo]
    ukupna_cijena: float


 
class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate : Optional[tuple[float,float]] =(0.0 , 0.0)
 

