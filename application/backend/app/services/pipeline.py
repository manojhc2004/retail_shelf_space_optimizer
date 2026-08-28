# pipe line  
from app.services.steps.network import NetWorkGraph
import pandas as pd
from fastapi import HTTPException,status
from app.services.steps.transaction import Transaction 
from app.services.steps.fp_growth import FPGrowth
from app.services.steps.association_rule import AssociationRule
from app.services.steps.final_rule import FinalRules
from app.services.steps.network import NetWorkGraph
from app.services.steps.engine import Engine
from app.schema.user_input import UserInput

from app.services.data_validator import DataValidator

class Pipeline:

    def run(self,df: pd.DataFrame, user_input:UserInput):
        
        # data validator 
        dv = DataValidator(df, user_input)
        data=dv.run_verify_() # for user input validation
        data=dv.validate_data()     # for df shape and null values
        data=dv.validate_columns()  # for column names
        data=dv.validate_dataype()  # for data types

        # Transaction
        te = Transaction(data)
        basket = te.transaction_()

        # FPGrowth 
        fp = FPGrowth()
        freq_item = fp.freq_items_(basket,user_input.min_support) # considered 0.005 as min support

        identified_freq = fp.identified_freq()

        filtered_items = fp.show_identified_freq(user_input.greater_than) 

        # Association Rule 
        ar = AssociationRule(freq_item)
        rules = ar.applyRule_(user_input.threshold)

        # final rule 
        fr = FinalRules()
        final_rules = fr.addRules(rules)


        # network graph 
        nw = NetWorkGraph()
        get_communities = nw.get_communities_(final_rules)

        # create interactive HTML
        html_path = nw.create_interactive_graph()
        
        # for plot 
        # nw.show_network_() 


        # engine
        engine = Engine()
        get_shelf = engine.shelf_engine_(get_communities,shelf_capacity=user_input.shelf_capacity)

        return get_shelf