from time import time
import ProcessData
import BuildingGraph
import networkx as nx
t0 = time()
graphs = []
train_labels, train_sents = ProcessData.PreprocessFile('./DataSet/r8-train-no-stop.txt')
test_labels, test_sents = ProcessData.PreprocessFile('./DataSet/r8-test-no-stop.txt')
i = 0
for doc in train_sents:
    G = BuildingGraph.builder(directed=False,weighted=False,window_size=4,inputDoc=doc)
    graphs.append(G)
    nx.write_gexf(G,'./R8/R8_nostop_graphgefx/docs_'+ str(i) +'.train.gexf')
    i += 1
print ("Time for building all graphs: "), time() - t0
print ("Number of graphs: "),len(graphs)