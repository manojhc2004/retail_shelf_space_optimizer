from config import *


class FinalRules:
    
    def addRules(self,rules):
        
        final_rules = rules[
            [
                "antecedents",
                "consequents",
                "support",
                "confidence",
                "lift"
            ]
        ].copy()
        
        final_rules["antecedents"] = final_rules["antecedents"].apply(lambda x: ", ".join(list(x)))

        final_rules["consequents"] = final_rules["consequents"].apply(lambda x: ", ".join(list(x)))
        
        final_rules = final_rules.sort_values(by="lift",ascending=False)
        
        logging.info("final rule applied")
        return final_rules