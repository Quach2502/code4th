import networkx as nx
import ProcessData
directed = False
weighted = True
window_size = 4
testDoc = "As a discipline, computer science spans a range of topics from theoretical studies of algorithms and the limits of computation to the practical issues of implementing computing systems in hardware and software."
def builder(directed,weighted,window_size,inputDoc):
    # inputDoc: String
    # directed: True for directed, False for undirected
    # weighted: True for weighted graph, False for unweighted graph
    inputDoc = ProcessData.ProcessDoc(inputDoc)
    # print inputDoc
    # for direction
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    # add edges and nodes
    for s in inputDoc:
        # Ignore the sentence with less than window_size words
        if len(s) >= window_size:
            for word in s:
                # print word
                G.add_node(word,name = word)
            window = list(s[:window_size])
            for i in range(len(s)):
                # print window
                for word in window[1:]:
                    if word != window[0]:
                        if G.has_edge(window[0],word):
                            G[window[0]][word]['weight'] += 1
                        else:
                            G.add_edge(window[0],word,weight=1)
                        # print window[0],word
                if i < (len(s) - window_size):
                    window.append(s[i+window_size])
                del window[0]
    return G
# graph = builder(directed,weighted,window_size,testDoc)
# nx.write_gml(graph,'test1.gml')