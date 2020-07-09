import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date

from .database import Base


class GlobalDailyCases(Base):
    __tablename__ = "daily_cases"
    index = Column(Integer, primary_key=True, nullable=False)
    country_region = Column(String)
    province_state = Column(String)
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)
    iso3 = Column(String)


class USADailyCases(Base):
    __tablename__ = "usa_covid19"
    index = Column(Integer, primary_key=True)
    country_region = Column(String)
    province_state = Column(String)
    county_city = Column(String)
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)


# if __name__ == "__main__":
#     from sqlalchemy.orm import Session
#     from sqlalchemy import create_engine

#     from connection import conn_string_proxy

#     engine = create_engine(conn_string_proxy)
#     global_daily_cases_db = Session(engine)
#     print(
#         [
                
#             for val in global_daily_cases_db.query(GlobalDailyCases).filter(
#                 GlobalDailyCases.iso3 == "BRA"
#             )
#         ]
#     )
