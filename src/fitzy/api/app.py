from fastapi import FastAPI

from fitzy.api.routers import bmi

app = FastAPI()
app.include_router(bmi.router)
