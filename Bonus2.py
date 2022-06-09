import imp
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
import imp

class Graph:
    
    def __init__(self):
        self.verticesnames=[]
        self.vertices=0
        self.graph = []
        
    def addEdge(self, u, v, w: float)->None: #  u to  v are vertices and float w is the directional weight
        if u not in self.verticesnames:
            self.verticesnames.append(u)
            self.vertices=len(self.verticesnames)
        if v not in self.verticesnames:
            self.verticesnames.append(v)
            self.vertices=len(self.verticesnames)
        self.graph.append([self.verticesnames.index(u),self.verticesnames.index(v),w])
        
    def BellmanFord(self, startvertices, endvertices)->None:
        distvec= [float("Inf")]*self.vertices 
        distvec[self.verticesnames.index(startvertices)]=0 
        
        for dummy in range(self.vertices-1):
            for u,v,w in self.graph:
                if distvec[u] != float("Inf") and distvec[u]+w <distvec[v]:
                    distvec[v] = distvec[u] + w
                    
        self.printSolution(distvec,startvertices,endvertices)
        
    def printSolution(self, distvec,startvertices,endvertices)->None:
        for i in range(self.vertices):
            if self.verticesnames.index(endvertices)==i:
                print(f"shortest path from {startvertices} to {endvertices} is {distvec[i]}")
                
    def addMatrix(self,matrix):
        for u,v,w in matrix:
            self.addEdge(u,v,w)
    
                
if __name__ == "__main__":

    # matrix=[['A', 'B', 1], # form A to B with weight 1
    # ['B', 'C', 4],
    # ['C','D', 4],
    # ['A','C',7],
    # ['A','E',12],
    # ['D','E',1]]
    
    nums=range(5,9)
    datamat=[]
    for num in nums:
        timedata=[]
        print(f"next num {num}")
        for dum in range(20):
            tic = time.perf_counter()
            N=2**num
            p=20/(N-1)
        
            G= nx.erdos_renyi_graph(N,p,True)
            edgelist=list(G.edges)
            matrix2=[]
            for x in edgelist:
                u,v = x;
                matrix2.append([u,v,1])
                
            #print(matrix2)
            #nx.draw(G, with_labels=True)
            #plt.show()

            graph = Graph()
            graph.addMatrix(matrix2)
            graph.BellmanFord(1,(2**num)-1)
            toc = time.perf_counter()
            timedata.append(toc-tic)
        datamat.append(timedata)
        
print(datamat)
datamatnp=np.array(datamat)
meantime=np.mean(datamatnp,axis=1)
plt.plot(nums,meantime)
plt.show()