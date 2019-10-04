class BellmanFord:

    def __init__(self, vertices):
        self.graph = []
        self.numberOfVertices = vertices
        
    def createGraph(self, u, v, w): 
	    self.graph.append([u, v, w])

    def printResults(self, dist, source): 
        print("Distance from: %d | Source>Distance>Outlet", source)
        for i in range(self.numberOfVertices):
            print("%d >\t%d\t> %d" % (source, dist[i], i))
    
    def execute(self, source):
        path_cost = float('inf')
        dist = [path_cost] * self.numberOfVertices
        dist[source] = 0
        for _ in range(self.numberOfVertices - 1):
            for u, v, w in self.graph:
                if dist[u] != path_cost and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != path_cost and dist[u] + w < dist[v]:
                print ("This Graph has negative weight cycle")
        self.printResults(dist, source)
    
    
    
