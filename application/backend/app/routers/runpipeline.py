from fastapi import APIRouter, UploadFile, File, Depends
from app.services.pipeline import Pipeline
from app.services.data_validator import read_dataframe
from app.schema.user_input import UserInput
import pandas as pd
import logging

run_pipeline_api = APIRouter()


@run_pipeline_api.post("/run_pipeline")
async def run_pipeline(file: UploadFile = File(...), user_input: UserInput = Depends(UserInput.as_form)):

    df = read_dataframe(file)
    logging.info("dataframe collected successfully")
    
    # print(df.head())
    result = Pipeline().run(df, user_input)
    
    logging.info("pipeline completed successfully")
    
    return {"message": "pipeline completed successfully",
            "summary":{"total_shelves": result["Shelf"].nunique(),
            "html_path":"static/network.html",
            "data":result.to_dict(orient="records")}}