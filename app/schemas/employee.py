from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    dept: str
    salary: float

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
