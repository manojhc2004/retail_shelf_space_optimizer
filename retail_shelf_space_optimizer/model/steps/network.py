from config import *

# class for network and graph
class NetWork:
    
        
    def show_network_(self,rule):  # pass 'final saved rule'
        
        G = nx.Graph()

        for _, row in rule.iterrows():
            G.add_edge(
                row["antecedents"],
                row["consequents"],
                weight=row["lift"]
            )
            
        plt.figure(figsize=(15,10))

        pos = nx.spring_layout(
            G,
            seed=42
        )

        nx.draw_networkx(
            G,
            pos,
            node_size=900,
            font_size=8)

        plt.title("Retail Product Association Network")

        plt.show()
        
        self.communities = list(greedy_modularity_communities(G))
        logging.info("plotted netword graph")
    
    def get_shelf(self):
        
        return self.communities  