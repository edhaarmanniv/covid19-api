from typing import List
from datetime import date, timedelta

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

start_date_default = date.fromisoformat("1970-01-01") 
end_date_default = date.today() - timedelta(days=1) # need to integrate "most recent date" into route function
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


@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records


@app.get("/API/Global", response_model=List[schemas.GlobalDailyCases])
async def global_route(
    db: Session = Depends(get_db),
    start_date: date = start_date_default,
    end_date: date = end_date_default,
    iso3: str = iso3_default,
):
    return


@app.get("/API/US", response_model=List[schemas.USADailyCases])
async def usa_route(
    db: Session = Depends(get_db),
    start_date: date = start_date_default,
    end_date: date = end_date_default,
    state: str = state_default,
    county: str = county_default,
):
    return
