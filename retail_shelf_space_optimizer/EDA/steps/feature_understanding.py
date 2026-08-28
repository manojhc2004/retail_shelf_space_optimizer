class Features:
    
    def __init__(self,df):
        
        self.df = df
        
    def nunique(self,col):
        print()
        print("column :",col)
        print("Number - of Unique")
        print(self.df[col].nunique())
    
    def value_count(self,col):
        print()
        print("column :",col)
        print("Value - Counts")
        print()
        print(self.df[col].value_counts())
        
    def column(self,col):
      
        print(self.nunique(col))
        print(self.value_count(col))