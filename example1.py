from bellmanFord import BellmanFord

bf = BellmanFord(5)         #5 vertices
bf.createGraph(0, 1, -1)    #Adding a description of the graph
bf.createGraph(0, 2, 4) 
bf.createGraph(1, 2, 3) 
bf.createGraph(1, 3, 2) 
bf.createGraph(1, 4, 2) 
bf.createGraph(3, 2, 5) 
bf.createGraph(3, 1, 1) 
bf.createGraph(4, 3, -3) 
bf.execute(0)               #Execute an alghoritm