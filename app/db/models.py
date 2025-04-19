from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dept = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
