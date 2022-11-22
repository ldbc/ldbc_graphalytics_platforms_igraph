from igraph import *
import csv
import time

dataset = '/Users/szarnyasg/graphs/wiki-Talk'

g = Graph(directed=True)
g.es["weight"] = 1.0

start_time = time.time()
print("================================= Loading ====================================");
with open(dataset + '.e', 'r') as efile:
    g = Graph.Read(efile, format='ncol')
print("%.2f seconds" % (time.time() - start_time))

start_time = time.time()
print("=================================== BFS ====================================");
bfs = g.distances(source = 0, weights=None)
#print(bfs)
print("%.2f seconds" % (time.time() - start_time))

# start_time = time.time()
# print("=================================== SSSP ===================================");
# sssp = g.distances(source = 0, weights="weight")
# #print(sssp)
# print("%.2f seconds" % (time.time() - start_time))

start_time = time.time()
print("=================================== WCC ====================================");
wcc = g.as_undirected().components()
#print(wcc)
print("%.2f seconds" % (time.time() - start_time))

# CDLP, LCC, and PR give different results or lack support for some cases

# # different results due to randomized algorithm
# print("=================================== CDLP ===================================");
# print(g.community_label_propagation())

# # directed definition is not supported
# print("=================================== LCC ====================================");
# print(g.as_undirected().transitivity_local_undirected())

# # different results due to fixed-point (eps) approach
# print("==================================== PR ====================================");
# print(g.pagerank())
