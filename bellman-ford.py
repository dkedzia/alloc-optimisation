class BellmanFord:

    def __init__(self, vertices):
        self.numberOfVertices = vertices
        self.graph = []

    def createGraph(self, u, v, w): 
	    self.graph.append([u, v, w])

    def printArr(self, dist, source): 
        print("Distance from: ", source)
        for i in range(self.numberOfVertices):
            print("% d \t\t % d" % (i, dist[i]))
    
    def execute(self, source):
        dist = [float("Inf")] * self.numberOfVertices
        dist[source] = 0
        for _ in range(self.numberOfVertices - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print ("Graph contains negative weight cycle")
                return
        self.printArr(dist, source)
    
    
    
bf = BellmanFord(5)
bf.createGraph(0, 1, -1) 
bf.createGraph(0, 2, 4) 
bf.createGraph(1, 2, 3) 
bf.createGraph(1, 3, 2) 
bf.createGraph(1, 4, 2) 
bf.createGraph(3, 2, 5) 
bf.createGraph(3, 1, 1) 
bf.createGraph(4, 3, -3) 
bf.execute(0)