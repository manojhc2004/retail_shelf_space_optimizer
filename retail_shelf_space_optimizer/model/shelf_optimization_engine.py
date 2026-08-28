import pandas as pd


class Engine:
    
    def shelf_engine(self,communities,shelf_capacity):

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
            return self.df
    
    def get_list(self):
        
        self.shelf_summary = self.df.groupby("Shelf")["Product"].apply(list)
        
        return self.shelf_summary
    
    def get_list_df(self):
        
        self.get_list_into_df = pd.DataFrame(self.shelf_summary)
        
        return self.get_list_into_df
        
    def save_list(self,df,title):
        
        df.to_csv(title)
        return "list saved"