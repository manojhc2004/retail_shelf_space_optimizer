from fastapi import FastAPI
from app.routers.runpipeline import run_pipeline_api

app = FastAPI()


app.include_router(run_pipeline_api)