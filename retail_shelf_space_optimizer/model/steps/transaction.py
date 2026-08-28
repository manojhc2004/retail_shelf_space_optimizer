from config import *

class Transaction:
    
    def __init__(self,df):
        
        self.df = df
        
    def transaction_(self):
        
        
        self.transactions = (self.df.groupby("order_id")['product_name'].
                        apply(list).
                        reset_index(name="items"))
        
        
        # encoder
        te = TransactionEncoder()

        # fitting the list of products to the 'TransactionEncoder' as te
        self.basket = te.fit(self.transactions["items"]).transform(self.transactions["items"])

        
        # now converting the basket type:bool to type:int
        #basket_into_integer = self.basket.astype(int)
        self.basket_int_df = pd.DataFrame(
            data= self.basket,
            columns=te.columns_
        )
        
        #logging.info("transaction completed")
        return self.basket_int_df