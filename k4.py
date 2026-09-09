# software for network analysis 
# will generate graphs and has many built in tools for graph theory
import networkx as nx
# used to generate plots
import matplotlib.pyplot as plt
import copy

# creates a test graph
'''G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3])
G.add_edges_from([(0, 1), (0, 2), (1,3), (2,3), (0,3)])'''

# function to test graph with conjecture
def check_conjecture(graph):
    
    # gets the number of vertices in the graph
    n = nx.number_of_nodes(graph)
    #print(n)
    # gets the number of egdes in the graph
    m = nx.number_of_edges(graph)
    #print(m)
    # gets the number of triangles in the graph
    t = sum(nx.triangles(graph).values()) / 3
    #print(t)
    # compute left side of conjecture inequality
    val = (3 * (n-3)) + (t/3) - m
    #print(val)

    #check conjecture
    if  val > 0:

        #print('conjecture holds')
        C = 0
    
    else:

        C = 1
        #print('fails conjecture')
    
    return C

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

     
def deleteEdges(list, g_list, v):

    num_nodes = v
    # create new graph
    G_new = nx.Graph()
    # add number of vertices of the graph
    node_list = []
    i = 0
    
    while i < num_nodes:
        node_list.append(i)
        i = i + 1

    G_new.add_nodes_from(node_list)
    # populate edges of the graph using the edge list
    G_new.add_edges_from(list)
    # draws the graph
    #nx.draw(G_new, with_labels=True, font_weight='bold')
    #plt.show()

    for graph in g_list:

        if nx.is_isomorphic(G_new, graph):
            #print('is iso')
            return
    
    else:
        g_list.append(G_new)

        # recursive formula for deleting edges
        # if every edge has been deleted stop
        
        if len(list) == 0:
            
            return

        else:
            
            # take an edge in the graph
            for edge in list:

                #print('working')
                # create a new list
                temp_list = copy.deepcopy(list)
                # remove the edge
                temp_list.remove(edge)
                G = nx.Graph()
                # add number of vertices of the graph
                G.add_nodes_from(node_list)
                # populate edges of the graph using the edge list
                G.add_edges_from(temp_list)
                # apply recursion to the temporary list
                deleteEdges(temp_list, g_list, v)

    return g_list

G = nx.read_graph6('6apex2m9.g6')   
# add u,v and edges to graphs
orig_graphs, edges, triangles = create_2_apex(G)
#print(orig_graphs)

if __name__ == "__main__":

    graphs = []
    graph_list = []
    bad_graphs = []



    #print(orig_graphs[0])

    # create an edge list from a given graph
    e_list = list(orig_graphs[0].edges)
    #print(e_list)
    vertices = nx.number_of_nodes(orig_graphs[0])
    
    # gets all possible graphs from deleted edges
    graphs = deleteEdges(e_list, graph_list, vertices)
    #print(graphs)
    print(len(graphs))
    '''for i in graphs:
        nx.draw(i, with_labels=True, font_weight='bold')
        plt.show()'''
        
    '''# check conjecture for leftover graphs
    for i in graphs:
        val = check_conjecture(i)
        if val == 1:
            bad_graphs.append(i)
        #nx.draw(i, with_labels=True, font_weight='bold')
        #plt.show()

    print(bad_graphs)
    print(len(bad_graphs))
    
    plt.show()'''
