import networkx as nx
import matplotlib.pyplot as plt

 
def create_2_apex(G):

    """adds edges u,v to each graph in g6 file stores each to a list, returns the number of edges and triangles for each graph

        Parameters
        ----------
        G : list
            The list of graphs from the .g6 file

        ------
       Returns
            graphs, edges, triangles
    """
    graphs = []
    edges = []
    triangles = []

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

        
        m = int(i.number_of_edges())

        t = nx.triangles(i)

        num_t = int(sum(t.values()) / 3)

        # add updated graph, edges, and triangles to list
        graphs.append(i)
        edges.append(m)
        triangles.append(num_t)



    return graphs, edges, triangles
    

def check_conjecture(graph):

    """function to check the conjecture given vertices, triangles, and edges
        Parameters
        ----------
        graph : 
            The graph you are attempting to check
    
        ------
       Returns
            C :
                As a 1 when conjecture fails or a zero when conjecture holds
    """
    
    
    n = nx.number_of_nodes(graph)
    m = nx.number_of_edges(graph)
    t = sum(nx.triangles(graph).values()) / 3
    
    # compute left side of conjecture inequality
    val = (3 * (n-3)) + (t/3) - m
    
    if  val >= 0:

        C = 0
    
    else:

        C = 1
    
    return C


def delete_edge_check_u(G):

    """function to check the conjecture given vertices, triangles, and edges while deleting edges from vetex u
        Parameters
        ----------
        graph : 
            The graph you are attempting to check
    
        ------
       Returns
            bad_graphs :
                A list of graphs that fail to satisfy the conjecture
    """

    bad_graphs = []

    graph = G
    
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    n = 0
    while n < 6:
        
        graph.remove_edge(6, n) 

        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

        m = int(graph.number_of_edges())
        t = nx.triangles(graph)
        num_t = int(sum(t.values()) / 3)

        conjecture = check_conjecture(6, num_t, m)
        
        if conjecture == 1:

            bad_graphs.append(graph)

        n = n + 1

    return bad_graphs

def delete_edge_check_v(G):

    """function to check the conjecture given vertices, triangles, and edges while deleting edges from vertex v
        Parameters
        ----------
        G : 
            The graph you are attempting to check
    
        ------
       Returns
            bad_graphs :
                A list of graphs that fail to satisfy the conjecture
    """

    bad_graphs = []

    graph = G
    
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    n = 0
    while n < 6:
        
        print(n)
        graph.remove_edge(6, n) 

        m = int(graph.number_of_edges())
        t = nx.triangles(graph)
        num_t = int(sum(t.values()) / 3)

        conjecture = check_conjecture(6, num_t, m)
        
        if conjecture == 1:

            bad_graphs.append(graph)

        n = n + 1

    return bad_graphs
            
if __name__ == "__main__":


    G = nx.read_graph6('7apex2m11.g6')

    # add u,v and edges to graphs
    graphs, edges, triangles = create_2_apex(G)
    
    f_graphs = []

    i = 0

    while i < len(G):

        #delete edges and check conjecture for first graph
        #delete_edge_check_u(graphs[i])

        #delete edges and check conjecture for first graph
        c = check_conjecture(G[i])

        if c == 1:  

            f_graphs.append(G[i])
            n = nx.number_of_nodes(G[i])
            m = nx.number_of_edges(G[i])
            t = sum(nx.triangles(G[i]).values()) / 3
            print(i + 1, "n = ", n,  "m = ", m,  "t = ", t)

        i = i + 1
    
    if len(f_graphs) > 0:
        print("f graphs", f_graphs)
        G_new = f_graphs[0]
        print(len(f_graphs))
        nx.draw(G_new, with_labels=True, font_weight='bold')
        plt.show()
    else:
        print("all graphs satisfy inequality")




