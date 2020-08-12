import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date

from .database import Base


class GlobalDailyCases(Base):
    __tablename__ = "daily_cases"
    index = Column(Integer, primary_key=True, nullable=False)
    country_region = Column(String(255))
    province_state = Column(String(255))
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)
    iso3 = Column(String(255))


class USADailyCases(Base):
    __tablename__ = "usa_covid19"
    index = Column(Integer, primary_key=True)
    country_region = Column(String(255))
    province_state = Column(String(255))
    county_city = Column(String(255))
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
