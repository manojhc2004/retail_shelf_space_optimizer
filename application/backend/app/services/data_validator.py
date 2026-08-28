from app.schema.user_input import UserInput
from fastapi import HTTPException,status
import pandas as pd 
import logging


def read_dataframe(file):
    try:
        if file.filename.endswith("csv"):
            return pd.read_csv(file.file)
        elif file.filename.endswith("xlsx"):
            return pd.read_excel(file.file)
        elif file.filename.endswith("json"):
            return pd.read_json(file.file)
        else:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                                detail="Supports only csv,xlsx and json")
    except Exception as e:
        logging.error("File loaded failed")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


class DataValidator:

    def __init__(self,df:pd.DataFrame, user_input: UserInput):
        self.df = df
        self.user_input = user_input
        self.score = 0

    def run_verify_(self):

        try:
            if self.user_input.min_support <= 0.003 or self.user_input.min_support > 0.02:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="min_support must be between 0 and 1")
            if self.user_input.threshold <= 0.05 or self.user_input.threshold > 0.95:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="threshold must be between 0 and 1")
            if self.user_input.shelf_capacity <= 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="shelf_capacity must be greater than 0")
            if self.user_input.greater_than <= 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="greater_than must be greater than 0")
            logging.info("User input is valid")
            self.score += 1

        except Exception as e:
            logging.error("User input is invalid")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    def validate_data(self): 

        # check if dataframe is empty
        # check if datafram is having missing or null values
        # check if dataframe has less than 10 columns
        # check if dataframe has only 2 columns
        # check if dataframe has only object type
        # check dataframe shape

        if self.df.empty:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Dataframe is empty")
            logging.error("Dataframe is empty")

        if self.df.isna().any().any():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Dataframe has missing or null values")
            logging.error("Dataframe has missing or null values")

        if self.df.shape[1] > 10:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Data must have less than 10 columns")
            logging.error("Dataframe has more than 10 columns")

        if self.df.shape[1] < 2:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Data must have at least 2 columns")
            logging.error("Dataframe has less than 2 columns")

        if self.df.shape[0] < 5000:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Data must have at least 5000 rows")
            logging.error("Dataframe has less than 5000 rows")

        self.score += 1

    def validate_columns(self):

        # check if 'order_id', and 'product_name' are present

        if self.df['order_id'].empty or self.df['product_name'].empty:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Dataframe must have 'order_id' and 'product_name' columns")
            logging.error("Dataframe must have 'order_id' and 'product_name' columns")
        self.score += 1

    def validate_dataype(self):

        
        # check if "order_id:int" and "product_name:str" or not?
        if self.df['order_id'].dtype != 'int64' or self.df['product_name'].dtype != 'str':
            self.df['order_id'] = self.df['order_id'].astype(int)
            self.df['product_name'] = self.df['product_name'].astype(str)
            logging.info("Dataframe columns are converted to the correct format")
        else:
            logging.info("Dataframe columns are already in the correct format")

        self.score += 1

        if self.score == 4:
            logging.info("Dataframe is validated and returned final dataframe")
            return self.df
        else:
            logging.error("Dataframe is not validated and returned False")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Dataframe is not validated and returned False")


# required data type
""" 
 0   order_id        10000 non-null  int64  
 1   user_id            10000 non-null  int64  
 2   order_date         10000 non-null  str    
 3   time               10000 non-null  str    
 4   order_hour_of_day  10000 non-null  int64  
 5   product_name       10000 non-null  str    
 6   quantity           10000 non-null  int64  
 7   price              10000 non-null  float64
 8   category           10000 non-null  str    
 9   product_id         10000 non-null  int64  """