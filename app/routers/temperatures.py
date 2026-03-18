from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db
from .. import crud, models
from ..services.weather import fetch_temperature

router = APIRouter(prefix="/temperatures", tags=["Temperatures"])


@router.post("/update")
async def update_temperatures(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()

    results = []
    for city in cities:
        temp = await fetch_temperature(city.name)
        record = crud.create_temperature(db, city.id, temp)
        results.append(record)

    return results


@router.get("/")
def get_all(city_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_temperatures(db, city_id)
