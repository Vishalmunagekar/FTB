from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.db.models import Employee
from app.schemas.employee import EmployeeCreate, EmployeeOut, EmployeeUpdate
from typing import List

router = APIRouter()

@router.post("/employees", response_model=EmployeeOut)
async def create_employee(emp: EmployeeCreate, db: AsyncSession = Depends(get_db)):
    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    await db.commit()
    await db.refresh(new_emp)
    return new_emp

@router.get("/employees", response_model=List[EmployeeOut])
async def list_employees(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee))
    return result.scalars().all()

@router.get("/employees/{emp_id}", response_model=EmployeeOut)
async def get_employee(emp_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee).where(Employee.id == emp_id))
    emp = result.scalar_one_or_none()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/employees/{emp_id}", response_model=EmployeeOut)
async def update_employee(emp_id: int, emp_data: EmployeeUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee).where(Employee.id == emp_id))
    emp = result.scalar_one_or_none()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp_data.dict().items():
        setattr(emp, key, value)

    await db.commit()
    await db.refresh(emp)
    return emp

@router.delete("/employees/{emp_id}")
async def delete_employee(emp_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee).where(Employee.id == emp_id))
    emp = result.scalar_one_or_none()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    await db.delete(emp)
    await db.commit()
    return {"detail": f"Employee with id {emp_id} deleted"}
