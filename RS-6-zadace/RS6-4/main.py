from fastapi import FastAPI
from routers import films

app = FastAPI(
    title="Film mikroservis",
    description="Mikroservis za dohvaćanje podataka o filmovima",
    version="1.0.0"
)

app.include_router(films.router, prefix="/films")
