from pydantic import BaseModel, Field

class BaseCar(BaseModel):
    marka: str
    model: str 
    boja: str
    godina_proizvodnje: int
    cijena: int 
class CarRequest(BaseCar):
    pass

class CarResponse(BaseCar):
    id: int 
    cijena_pdv: int