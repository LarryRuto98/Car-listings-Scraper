# src/db/database.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class CarDB(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    price = Column(Float)
    currency = Column(String)
    mileage = Column(Float)
    fuel_type = Column(String)
    transmission = Column(String)
    engine_size = Column(String)
    location = Column(String)
    seller_type = Column(String)
    url = Column(String)
    raw_title = Column(String)
    scraped_date = Column(Date)

# 🔹 Database connection 
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Create tables if not exist"""
    Base.metadata.create_all(engine)
