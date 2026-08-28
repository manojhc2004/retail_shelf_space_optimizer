import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib.pyplot as plt
from pyvis.network import Network
import os
# class for network and graph
class NetWorkGraph:
    
        
    def get_communities_(self,rule):  # pass 'final saved rule'
        
        self.G = nx.Graph()

        for _, row in rule.iterrows():
            self.G.add_edge(
                row["antecedents"],
                row["consequents"],
                weight=row["lift"]
            )

        
        self.communities = list(greedy_modularity_communities(self.G))
        #logging.info("plotted netword graph")

        return self.communities

    def create_interactive_graph(self):

        net = Network(
            height="700px",
            width="100%",
            bgcolor="white",
            font_color="black"
        )

        net.from_nx(self.G)

        os.makedirs("app/static", exist_ok=True)

        output_path = "app/static/network.html"

        net.save_graph(output_path)

        return output_path

    def show_network_(self):

        plt.figure(figsize=(15, 10))

        # Fixed node positions
        pos = nx.spring_layout(self.G, seed=42)

        # Edge weights (lift)
        edge_weights = [
            self.G[u][v]["weight"]
            for u, v in self.G.edges()
        ]

        nx.draw_networkx(
            self.G,
            pos,
        node_color="skyblue",
        node_size=1000,
        font_size=8,
        font_weight="bold",
        width=edge_weights,      # Stronger lift = thicker edge
        edge_color="gray"
        )

        plt.title("Retail Product Association Network", fontsize=16)
        plt.axis("off")
        plt.tight_layout()
        plt.show()