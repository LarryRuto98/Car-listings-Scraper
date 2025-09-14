# src/models/car.py

from datetime import datetime

class Car:
    def __init__(self, brand, model, year, price, currency,
                 mileage=None, fuel_type=None, transmission=None,
                 engine_size=None, location=None, seller_type=None,
                 url=None, raw_title=None, scraped_date=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.currency = currency
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.engine_size = engine_size
        self.location = location
        self.seller_type = seller_type
        self.url = url
        self.raw_title = raw_title
        self.scraped_date = scraped_date or datetime.today().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert to dictionary (useful for DataFrame or JSON)."""
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "currency": self.currency,
            "mileage": self.mileage,
            "fuel_type": self.fuel_type,
            "transmission": self.transmission,
            "engine_size": self.engine_size,
            "location": self.location,
            "seller_type": self.seller_type,
            "url": self.url,
            "raw_title": self.raw_title,
            "scraped_date": self.scraped_date,
        }
