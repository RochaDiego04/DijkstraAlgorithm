import heapq

class Edge:
    def __init__(self,  weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node that we come to this node
        self.predecessor = None
        # neighbors of the node
        self.neighbors = []
        self.min_distance = float("inf")
    
    # If current node's min_distance is less than other node, 
    # this function will return True.
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            # pop element with lowest distance, in the index[0], the heap will put the element with minimum distance and it will be popped out
            actual_vertex = heapq.heappop(self.heap) 
            if actual_vertex.visited:
                continue
            # Consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                    # We will insert 2 min distances in the same node
                    # So we will compare them to see which is lower
                    # [F-19][F-17]
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex): # Vertex which we want to go from current vertex
        print(f"The shortest path to the vertex is {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None: # Calculate till destination vertex has no more Node predecessors
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor

'''     IMPLEMENTATION      '''
# Step 1 - Create Nodes
nodeA1 = Node("A1")
nodeA2 = Node("A2")
nodeA3 = Node("A3")
nodeA4 = Node("A4")

nodeB1 = Node("B1")
nodeB2 = Node("B2")
nodeB3 = Node("B3")
nodeB4 = Node("B4")

nodeC1 = Node("C1")
nodeC2 = Node("C2")
nodeC3 = Node("C3")
nodeC4 = Node("C4")

nodeD1 = Node("D1")
nodeD2 = Node("D2")
nodeD3 = Node("D3")
nodeD4 = Node("D4")

# Step 2 - Create Edges
nodeA1.add_edge(5, nodeA2)
nodeA1.add_edge(7, nodeB1)
nodeA1.add_edge(8, nodeB2)

nodeB1.add_edge(9, nodeA2)
nodeB1.add_edge(7, nodeB2)
nodeB1.add_edge(4, nodeC2)
nodeB1.add_edge(5, nodeC1)

nodeC1.add_edge(1, nodeB2)
nodeC1.add_edge(3, nodeC2)
nodeC1.add_edge(8, nodeD2)
nodeC1.add_edge(10, nodeD1)

nodeD1.add_edge(2, nodeC2)
nodeD1.add_edge(5, nodeD2)
##########################
nodeA2.add_edge(6, nodeA3)
nodeA2.add_edge(1, nodeB3)
nodeA2.add_edge(5, nodeB2)

nodeB2.add_edge(2, nodeA3)
nodeB2.add_edge(7, nodeB3)
nodeB2.add_edge(8, nodeC3)
nodeB2.add_edge(9, nodeC2)

nodeC2.add_edge(10, nodeB3)
nodeC2.add_edge(7, nodeC3)
nodeC2.add_edge(9, nodeD3)
nodeC2.add_edge(2, nodeD2)

nodeD2.add_edge(1, nodeC3)
nodeD2.add_edge(8, nodeD3)
##########################
nodeA3.add_edge(3, nodeA4)
nodeA3.add_edge(2, nodeB4)
nodeA3.add_edge(1, nodeB3)

nodeB3.add_edge(9, nodeA4)
nodeB3.add_edge(10, nodeB4)
nodeB3.add_edge(4, nodeC4)
nodeB3.add_edge(5, nodeC3)

nodeC3.add_edge(8, nodeB4)
nodeC3.add_edge(11, nodeC4)
nodeC3.add_edge(20, nodeD4)
nodeC3.add_edge(3, nodeD3)

nodeD3.add_edge(6, nodeC4)
nodeD3.add_edge(2, nodeD4)
##########################
nodeA4.add_edge(5, nodeB4)

nodeB4.add_edge(1, nodeC4)

nodeC4.add_edge(9, nodeD4)

# Step 3 - Call Dijkstra Algorythm

algorithm = Dijkstra()
algorithm.calculate(nodeA1)
algorithm.get_shortest_path(nodeD4)