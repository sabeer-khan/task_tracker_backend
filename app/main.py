from fastapi import FastAPI
from app.routers import user, protected, task

app = FastAPI()

app.include_router(user.router)
app.include_router(protected.router)
app.include_router(task.router)
