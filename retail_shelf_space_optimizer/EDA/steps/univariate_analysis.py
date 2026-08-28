import matplotlib.pyplot as plt
import seaborn as sns  
import pandas as pd

class Univariate_Analysis:
    
    def __init__(self,df):
        
        self.df = df

    def bar(self, col1, col2, title):
        
        total_orders_by_product = (
            self.df.groupby(col1)[col2].count().reset_index()
        )
        total_orders_by_product = total_orders_by_product.sort_values(
            by=col2, ascending=False
        )

        # 1. Force explicit structural subplots with a wide aspect ratio
        fig, ax = plt.subplots(figsize=(22, 6))

        # 2. Bind the plot explicitly to the wide axes ('ax')
        sns.barplot(
            data=total_orders_by_product,
            x=col1,
            y=col2,
            palette="muted",
            ax=ax,
        )

        ax.set_title(title)
        ax.set_xlabel(col1)
        ax.set_ylabel("Order Count")

        # 3. Use 90 degrees with center alignment to prevent vertical text stacking
        ax.set_xticklabels(
            ax.get_xticklabels(), rotation=90, ha="center", fontsize=9
        )

        # 4. Explicitly scale the layout margins
        plt.subplots_adjust(bottom=0.3)
        plt.tight_layout()
        plt.show()

        return total_orders_by_product.describe()

        
    def line_with_unique(self,col1,col2,title):
        
        total = self.df.groupby(col1)[col2].nunique()
        
        plt.figure(figsize=(12,5))
        plt.plot(total.index,total.values, marker='o')
        plt.title(title)
        plt.xlabel(f"{col1}")
        plt.ylabel(f"{col2}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
    
    def line_with_noneunique(self,col1,col2,title):
        
        total = self.df.groupby(col1)[col2].count()
        
        plt.figure(figsize=(12,5))
        plt.plot(total.index,total.values, marker='o')
        plt.title(title)
        plt.xlabel(f"{col1}")
        plt.ylabel(f"{col2}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
        
    def dist(self,col,title):
        
        total  = self.df[col].sum()
        plt.figure(figsize=(12,5))
        sns.histplot(data=self.df, x=col, kde=True, color="royalblue", bins=30)
        plt.title(title)
        plt.xlabel(col)
        plt.show()
        
        print(f"\nTotal Sum is: {total}")
    
    def kde(self,col,title):
        
        plt.figure(figsize=(12,5))
        sns.kdeplot(data=self.df, x=col, fill=True, color="royalblue", alpha=0.3)
        plt.title(f"{title} {col}")
        plt.xlabel(col)
        plt.show()
        
    
    def col_quantity(self,col):
        
        ncustomer = self.df[col]
        
        print("total number of customer:",ncustomer.nunique())
        
        return self.df[col].describe()
    
    
    def normal_bar(self,col1,col2,title):
        
        
        total_orders_by_product = (
                    self.df.groupby(col1)[col2].count().reset_index()
                )
        total_orders_by_product = total_orders_by_product.sort_values(
                    by=col2, ascending=False
                )
    
        plt.figure(figsize=(12,5))
        sns.barplot(
        data=total_orders_by_product,
        x=col1,
        y=col2,
        palette="muted")
        plt.title(title)
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.show()
        
        return total_orders_by_product