import matplotlib.pyplot as plt
import networkx as nx 

# G = nx.Graph()

# G.add_nodes_from( [ (1, {'color':'red'}), 
#                     (2, {'color':'blue'}) ] )
# G.add_edge(1,2)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

G = nx.petersen_graph()

subax1 = plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()