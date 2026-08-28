import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class Multivariate_Analysis:
    
    def __init__(self,df):
        
        self.df = df
        
    
    def multi_for_revenue_unstack(self,col1,col2,col3):
        
        curr = self.df.groupby([col1,col2])[col3].sum().unstack(fill_value=0)

        return curr
        
    def multi_for_count(self,col1,col2,col3):
        
        month_hour = (
            self.df.groupby([col1, col2])[col3]
            .count()
            .unstack(fill_value=0))

        # Add total row
        month_hour.loc["Total"] = month_hour.sum()

        return month_hour
    
    def multi_for_revenue(self,col1,col2,col3):
        
        
        category_product = (
        self.df.groupby([col1, col2])[col3]
        .sum()
        .sort_values(ascending=False))
    
        return category_product