# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt

i = 10
# Defining a Class
class GraphVisualization:

    def __init__(self):

        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
G = GraphVisualization()
while i > 0:
    w = i
    while w != 1:
        if w % 2 != 0:
            G.addEdge(w,w*3+1)
            w = int(w*3+1)
        else:
            G.addEdge(w,int(w/2))
            w = int(w/2)
    i -= 1
# Driver code
G.visualize()
