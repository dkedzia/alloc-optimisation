class BellmanFord:
    numberOfVertices = 0
    def __init__(self, vertices):
        BellmanFord.numberOfVertices = vertices
    
    def execute(self):
        print(BellmanFord.numberOfVertices)

bf = BellmanFord(5)

bf.execute()