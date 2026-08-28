from mlxtend.frequent_patterns import association_rules

class AssociationRule:
    
    def __init__(self,freq_items):
        self.freq_items = freq_items
        
    def applyRule_(self,threshold=0.10):
        rules = association_rules(
        self.freq_items,
        metric = "confidence",
        min_threshold = threshold)
        
        
        rules = rules.sort_values(by="lift",
                                  ascending=False)
        
        #logging.info("association rule applied")
        return  rules