from datetime import date
from typing import Optional
from pydantic import BaseModel

class GlobalDailyCases(BaseModel):
    
    index : int 
    country_region : str
    province_state : str
    lat : Optional[float]
    long : Optional[float]
    date : date
    confirmed : Optional[int]
    deaths : Optional[int]
    recovered : Optional[int]
    iso3 : str

    class Config:
        orm_mode = True


class USADailyCases(BaseModel):
    
    index : int
    country_region : str 
    province_state : str
    county_city : str
    lat : Optional[float]
    long : Optional[float]
    date : date
    confirmed : Optional[int]
    deaths : Optional[int]

    class Config:
        orm_mode = True
