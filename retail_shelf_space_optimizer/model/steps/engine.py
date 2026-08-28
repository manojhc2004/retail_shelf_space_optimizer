from config import *

class Engine:
    
    def shelf_engine_(self,communities,shelf_capacity=4):

            shelf_data = []
            shelf_no = 1

            for community in communities:

                community = list(community)

                for i in range(0, len(community), shelf_capacity):

                    shelf_products = community[i:i+shelf_capacity]

                    for product in shelf_products:

                        shelf_data.append({
                            "Shelf": f"Shelf {shelf_no}",
                            "Product": product
                        })

                    shelf_no += 1

            self.df=  pd.DataFrame(shelf_data)
            
            # logging.info("shelf list returned successfully")
            return self.df
    
    
    def get_list_(self):
        
        self.shelf_summary = self.df.groupby("Shelf")["Product"].apply(list)
        
        return self.shelf_summary
    
    def save_list(self,title):
        
        #logging.info("shelf items saved successfully")
        self.shelf_summary.to_csv(title,index=False)