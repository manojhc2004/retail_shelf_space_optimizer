class Basic_inspection:
    
    def __init__(self,df):
        self.df = df
        
    def shape(self):
        self.shape =self.df.shape
        print("the number of rows:", self.shape[0])
        print("the number of columns:", self.shape[1])
    
    def describe(self):
        print("data describe")
        return self.df.describe()

    
    def nullvalues(self):
        print("identifying the null values")
        check_null = self.df.isna().sum()
        return check_null
    
    def info(self):
        print("data information")
        return self.df.info()