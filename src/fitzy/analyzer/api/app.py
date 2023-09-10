from fastapi import FastAPI

from fitzy.analyzer.api.routers import bmi

app = FastAPI()
app.include_router(bmi.router)
