import matplotlib.pyplot as plt
import seaborn as sns  
import pandas as pd



class Bivariate_Analysis:
    
    def __init__(self,df):
        
        self.df = df
        
    
    def bar_for_revenue(self,col1,col2,title):
        
        curr = self.df.groupby(col1)[col2].sum().sort_values(ascending=False).reset_index()
        
        plt.figure(figsize=(9,5))
        sns.barplot(data=curr.head(7), x=col1,y=col2)
        plt.title(title)
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.xticks(rotation=45)

        plt.show()
        
        return curr.head()


    # special plot for finding the repeat and none-repeat customers
    
    def find_repeat_customers(self):
        customer_month = (self.df.groupby(["month", "user_id"])["order_id"]
            .nunique()
            .reset_index(name="total_orders"))

        count_repeat_customers_by_month = customer_month.groupby("month")["user_id"].nunique().sort_values(ascending=False)
        
        plt.figure(figsize=(12,5))
        plt.bar(count_repeat_customers_by_month.index,count_repeat_customers_by_month.values)
        plt.xlabel("month")
        plt.ylabel("count")
        plt.title("number of repeat-customers by month")
        plt.show()
        
        return count_repeat_customers_by_month