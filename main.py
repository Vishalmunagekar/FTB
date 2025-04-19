from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine, Base

app = FastAPI(title="Employee CRUD App")

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def root():
    return {"message": "Welcome to the Employee CRUD App"}
