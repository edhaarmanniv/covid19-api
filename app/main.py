from typing import List
from datetime import date, timedelta

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from starlette.responses import RedirectResponse

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

start_date_default = date.fromisoformat("1970-01-01")
# end_date_default = date.today() - timedelta(days=1) # need to integrate "most recent date" into route function
iso3_default = "ALL"
state_default = "ALL"
county_default = "ALL"

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/API/Global", response_model=List[schemas.GlobalDailyCases])
async def global_route(
    db: Session = Depends(get_db),
    start_date: date = start_date_default,
    end_date: date = get_db().query(func.max(GlobalDailyCases.date)),
    iso3: List[str] = Query(
        iso3_default,
        title="ISO3",
        description="ISO3 Country Code - to query multiple countries include a 'iso3=' field for each one in the query string.",
        max_length=3,
    ),
):
    results = db.query(models.GlobalDailyCases).filter(
        GlobalDailyCases.date.between(start_date, end_date)
    )

    if iso3 != iso3_default:
        results = results.filter(GlobalDailyCases.iso3 == iso3)

    return results.all()


@app.get("/API/US", response_model=List[schemas.USADailyCases])
async def usa_route(
    db: Session = Depends(get_db),
    start_date: date = start_date_default,
    end_date: date = end_date_default,
    state: str = state_default,
    county: str = county_default,
):

    results = db.query(models.USADailyCases).filter(
        USADailyCases.date.between(start_date, end_date)
    )

    if state != state_default:
        results = results.filter(USADailyCases.province_state == state)

    if county != county_default:
        results = results.filter(USADailyCases.county == county)

    return results.all()
