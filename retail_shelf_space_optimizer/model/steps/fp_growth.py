from config import *

class FPGrowth:
    
    def freq_items_(self,basket_df,min=0.005):
        
        # training fp-growth
        self.freq_items = fpgrowth(
                    basket_df,
                    min_support=min,
                    use_colnames=True
                    )
    
        self.freq_items = self.freq_items.sort_values(
                        by="support",
                        ascending=False)
        
        logging.info("frequent items returned")
        return self.freq_items
    
    def identified_freq(self):
        
        self.freq_items["length"] = self.freq_items["itemsets"].apply(len)

        val_count = self.freq_items["length"].value_counts()
        
        logging.info(f"{val_count} returned")
        return val_count
    
    def show_identified_freq(self,greater_than=1):  
        
        combinations = self.freq_items[
        self.freq_items["length"] > greater_than].sort_values("support", ascending=False)
        
        return combinations