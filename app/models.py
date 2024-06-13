from sqlalchemy import Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Configuration(Base):
    __tablename__ = "configurations"

    country_code = Column(String, primary_key=True, index=True)
    requirements = Column(JSON, nullable=False)
