import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# mlxtend 
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

# network graph
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib.pyplot as plt

# sklearn
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer