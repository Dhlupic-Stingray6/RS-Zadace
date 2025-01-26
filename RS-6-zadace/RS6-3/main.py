from fastapi import FastAPI, HTTPException, status, Path, Query
from models import CarRequest, CarResponse
from typing import Optional

app = FastAPI()


automobili = [ 
    {"id":1, "marka":"Audi", "model":"A4", "boja":"crvena", "godina_proizvodnje":2018, "cijena":25000},
    {"id":2, "marka":"Mazda", "model":"6", "boja":"plava", "godina_proizvodnje":2010, "cijena":9500},
    {"id":3, "marka":"Ford", "model":"Fiesta", "boja":"bijela", "godina_proizvodnje":2015, "cijena":5000},
    {"id":4, "marka":"Jaguar", "model":"F-type", "boja":"crna", "godina_proizvodnje":2016, "cijena":50000},

]


@app.get('/automobil/{id}', response_model=CarRequest)
def dohvati_automobil(
    id: int, 
    min_cijena: Optional[int] = Query(0, gt=0, description="Minimalna cijena mora biti veća od 0"), 
    min_godina: Optional[int] = Query(1961, gt=1960, description="minimalna godina proizvodnje mora veća od 1960"),
    max_cijena: Optional[int] = Query(None),
    max_godina: Optional[int] = Query(None, le=2025)
    ):

    auto = next((auto for auto in automobili if auto['id'] == id), None)
    if not auto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Automobil nije pronađen"
        )


    if min_cijena or max_cijena <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Upisana cijena mora biti veća od 0!')
    
    
    if max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimalna cijena ne može biti veća od maksimalne cijene"
        )
    
    
    if max_godina is not None and min_godina > max_godina:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimalna godina proizvodnje ne može biti veća od maksimalne godine proizvodnje"
        )
    
    return auto


@app.post('/automobili/', response_model=CarResponse)
def dodaj_automobil(car_request : CarRequest):
    for auto in automobili:
        if auto["marka"].lower() == car_request.marka.lower() and \
           auto["model"].lower() == car_request.model.lower() and \
           auto["godina_proizvodnje"] == car_request.godina_proizvodnje:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Automobil već postoji u bazi podataka"
            )
        
    
    new_id = len(automobili) + 1
    cijena_pdv = car_request.cijena * 1.25


    novi_auto = {
        "id": new_id,
        "marka": car_request.marka,
        "model": car_request.model,
        "boja": car_request.boja,
        "godina_proizvodnje": car_request.godina_proizvodnje,
        "cijena": car_request.cijena,
        "cijena_pdv": cijena_pdv,
    }

    automobili.append(novi_auto)
    return novi_auto