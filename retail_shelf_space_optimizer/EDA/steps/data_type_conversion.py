import pandas as pd


class DataType:
    
    def __init__(self,df):
        self.df = df
        
    def to_datetime_(self,col,new_column_name):
        self.df[new_column_name] = pd.to_datetime(self.df[col])  
    
    def to_month_(self,col,new_column_name):
        
        self.df[new_column_name] = self.df[col].dt.month
        
    def to_time_(self,col,new_column_name):
        
        self.df[new_column_name] = pd.to_datetime(self.df[col], format="%H:%M:%S")
        
    
    def to_hour_(self,col,new_column_name):
        
        self.df[new_column_name] =  self.df[col].dt.hour
        
    
    def to_day_(self,col, new_column_name):
        
        self.df[new_column_name] = self.df[col].dt.day
    
    def to_dayname_(self,col, new_column_name):
        
        self.df[new_column_name] = self.df[col].dt.day_name()
    
    def weekend_and_weekday(self,col,new_column_name):
        
        self.df[new_column_name] = self.df[col].apply(lambda x: "Weekend" if x in ["Saturday", "Sunday"] else "Weekday")