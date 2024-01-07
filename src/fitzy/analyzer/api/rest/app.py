from fastapi import FastAPI

from fitzy.analyzer.api.rest.routers import bmi

app = FastAPI()
app.include_router(bmi.router)
