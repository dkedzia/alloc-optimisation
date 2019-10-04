class BellmanFord:

    def __init__(self, vertices):
        self.graph = []
        self.numberOfVertices = vertices

    def createGraph(self, fromV, toV, distanceToV): 
	    self.graph.append([fromV, toV, distanceToV])

    def printResults(self, dist, source): 
        print("Distance from: %d | Source>Distance>Outlet", source)
        for i in range(self.numberOfVertices):
            print("%d >\t%d\t> %d" % (source, dist[i], i))
    
    def execute(self, source):
        path_cost = float('inf')
        dist = [path_cost] * self.numberOfVertices
        dist[source] = 0
        for _ in range(self.numberOfVertices - 1):
            for fromV, toV, distanceToV in self.graph:
                if dist[fromV] != path_cost and dist[fromV] + distanceToV < dist[toV]:
                    dist[toV] = dist[fromV] + distanceToV
        for fromV, toV, distanceToV in self.graph:
            if dist[fromV] != path_cost and dist[fromV] + distanceToV < dist[toV]:
                print ("This Graph has negative weight cycle")
        self.printResults(dist, source)
    
    
    
