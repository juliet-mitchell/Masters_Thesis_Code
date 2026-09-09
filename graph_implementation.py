# software for network analysis 
# will generate graphs and has many built in tools for graph theory
import networkx as nx
# used to generate plots
import matplotlib.pyplot as plt

# adds edges u,v to each graph in g6 file stores each to a list
def create_2_apex(G):
    
    # create an empty list
    graphs = []
    edges = []
    triangles = []

    #iterate through the graphs in the g6 file
    for i in G:

        #add vertices u,v
        i.add_node(6, weight=0.4, UTM=("13S", 382871, 3972649))
        i.add_node(7, weight=0.4, UTM=("13S", 382971, 3972249))
        edge = 0

        # iterate through planar vertices add edge from vertex to u and v
        while edge < 6:

            i.add_edge(edge, 6)
            i.add_edge(edge, 7)
            edge = edge + 1

        # return number of edges
        m = int(i.number_of_edges())

        # finds number of trinagles for each node
        t = nx.triangles(i)

        # return number of triangles in the graph
        num_t = int(sum(t.values()) / 3)

        # add updated graph to list
        graphs.append(i)
        
        # add number of edges to list
        edges.append(m)
        
        # add number of triangles to the list
        triangles.append(num_t)



    return graphs, edges, triangles
    

# function to check the conjecture given vertices, triangles, and edges
def check_conjecture(graph):
    
    # gets the number of vertices in the graph
    n = nx.number_of_nodes(graph)
    #print("vertices", n)
    #print(n)
    # gets the number of egdes in the graph
    m = nx.number_of_edges(graph)
    #print("edges", m)
    #print(m)
    # gets the number of triangles in the graph
    t = sum(nx.triangles(graph).values()) / 3
    #print("triangles", t)
    # compute left side of conjecture inequality
    val = (3 * (n-3)) + (t/3) - m
    #print(val)

    #check conjecture
    if  val >= 0:

        #print('conjecture holds')
        C = 0
    
    else:

        C = 1
        #print('fails conjecture')
    
    return C


def delete_edge_check_u(G):

    bad_graphs = []

    graph = G
    
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    n = 0
    while n < 6:
        
        print(n)
        graph.remove_edge(6, n) 

        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

        # return number of edges
        m = int(graph.number_of_edges())

        # finds number of trinagles for each node
        t = nx.triangles(graph)

        # return number of triangles in the graph
        num_t = int(sum(t.values()) / 3)

        conjecture = check_conjecture(6, num_t, m)
        
        if conjecture == 1:

            bad_graphs.append(graph)

        n = n + 1

    return bad_graphs

def delete_edge_check_v(G, E, T):

    bad_graphs = []

    graph = G
    
    #nx.draw(G, with_labels=True, font_weight='bold')
    #plt.show()
    n = 0
    while n < 6:
        
        print(n)
        graph.remove_edge(6, n) 

        # return number of edges
        m = int(graph.number_of_edges())

        # finds number of trinagles for each node
        t = nx.triangles(graph)

        # return number of triangles in the graph
        num_t = int(sum(t.values()) / 3)

        conjecture = check_conjecture(6, num_t, m)
        
        if conjecture == 1:

            bad_graphs.append(graph)

        n = n + 1

    return bad_graphs
            
if __name__ == "__main__":

    # read graphs
    G = nx.read_graph6('7apex2m11.g6')
    #print(G)

    
    # add u,v and edges to graphs
    #graphs, edges, triangles = create_2_apex(G)
    
    f_graphs = []

    i = 0

    while i < len(G):

        #delete edges and check conjecture for first graph
        #delete_edge_check_u(graphs[i], edges[i], triangles[i])

        #delete edges and check conjecture for first graph
        c = check_conjecture(G[i])

        if c == 1:  

            f_graphs.append(G[i])
            n = nx.number_of_nodes(G[i])
            # gets the number of egdes in the graph
            m = nx.number_of_edges(G[i])
            # gets the number of triangles in the graph
            t = sum(nx.triangles(G[i]).values()) / 3
            print(i + 1, "n = ", n,  "m = ", m,  "t = ", t)

        i = i + 1
        #print(i)
    
    if len(f_graphs) > 0:
        print("f graphs", f_graphs)
        G_new = f_graphs[0]
        print(len(f_graphs))
        nx.draw(G_new, with_labels=True, font_weight='bold')
        plt.show()
    else:
        print("all graphs satisfy inequality")




