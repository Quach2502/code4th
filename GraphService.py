import networkx as nx
import copy
import BuildingGraph
import heapq

def core_Number(G, weighted):
    """
        Parameters
        ----------
        G : NetworkX graph
        weighted : boolean

        Returns
        -------
        core_number : dictionary
        A dictionary keyed by node to the core number.

        Notes
        -----
        Not implemented for graphs with parallel edges or self loops.
        For directed graphs the node degree is defined to be the
        sum of attached edges.
        Graph, node, and edge attributes are copied to the subgraph.

        References
        ----------
        [1] An O(m) Algorithm for Cores Decomposition of Networks
            Vladimir Batagelj and Matjaz Zaversnik,  2003.
            https://arxiv.org/abs/cs.DS/0310049
        [2] networkx source code
            https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/core.html
        """
    if weighted:
        GG = copy.deepcopy(G)
        cores = GG.degree(weight ='weight')
        nodes_list = get_Node_List(GG)
        weight_list = get_Weight_List(GG)
        heap_G = zip(weight_list,nodes_list)
        heapq.heapify(heap_G)
        # print heap_G
        while len(heap_G) > 0:
            top_vertex = heap_G[0][1]
            index_top = nodes_list.index(top_vertex)
            neighbor_top = GG.neighbors(top_vertex)
            cores[top_vertex] = weight_list[index_top]
            GG.remove_node(top_vertex)
            del nodes_list[index_top]
            del weight_list[index_top]
            if len(neighbor_top) > 0:
                for i in neighbor_top:
                    index_of_i = nodes_list.index(i)
                    max_i = max(cores[top_vertex],GG.degree(weight='weight')[i])
                    weight_list[index_of_i] = max_i
                    heap_G = zip(weight_list,nodes_list)
                    heapq.heapify(heap_G)
            else:
                #update heap
                heap_G = zip(weight_list,nodes_list)
                heapq.heapify(heap_G)
        return cores
    else:
        return nx.core_number(G)

def extract_K_Core(G,k,weighted):
    """
        Parameters
        ----------
        G : NetworkX graph
        weighted : boolean
        k: int, core_number

        Returns
        -------
        G : NetworkX graph
          The k-core subgraph

        References
        ----------
        [1] networkx source code
        https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/core.html
    """
    return nx.k_core(G,k,core_number=core_Number(G,weighted))

def extract_Main_Core(G,weighted):
    """
        Parameters
        ----------
        G : NetworkX graph
        weighted : boolean

        Returns
        -------
        G : NetworkX graph
          The main-core subgraph

    """
    return nx.k_core(G,core_number=core_Number(G,weighted))

def get_occurences(G,vocab):
    edge_weight_vocab = []
    for term in vocab.split('\n'):
        if term.startswith('e'):
            edge = term.split(' ')[-1]
            start_vert = edge.split('--')[0]
            end_vert = edge.split('--')[1]
            edge_weight = G[start_vert][end_vert]['weight']
            edge_weight_vocab.append(edge_weight)
            if edge_weight == 1:
                break
    return min(edge_weight_vocab)


# -----------------------------------------------Utility--------------------------------
def get_Weight_List(G):
    return [value for key, value in G.degree(weight='weight').items()]
def get_Node_List(G):
    return [key for key, value in G.degree(weight='weight').items()]


# testDoc = "A method for solution of systems of linear algebraic equations with m-dimensional lambda matrices. A system of linear algebraic equations with m-dimensional lambda matrices is considered. The proposed method of searching for the solution of this system lies in reducing it to a numerical system of a special kind."
# G = BuildingGraph.builder(directed=False,weighted=True,window_size=4,inputDoc=testDoc)
# nx.write_gml(G,'graphtesting.gml')
# nx.write_gml(extract_Main_Core(G,weighted = True),'coretesting.gml')
# print core_Number(G,weighted=True)
# print len(G.nodes())
