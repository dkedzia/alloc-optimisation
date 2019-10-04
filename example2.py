from bellmanFord import BellmanFord

bf = BellmanFord(5)         #5 vertices
bf.createGraph(0, 1, 1)    #Adding a description of the graph
bf.createGraph(0, 2, -7)
bf.createGraph(1, 2, 1)
bf.createGraph(2, 3, 1)
bf.createGraph(2, 4, 1)
bf.createGraph(3, 4, 1)


bf.execute(0)               #Execute an alghoritm