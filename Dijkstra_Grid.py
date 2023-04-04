import heapq
import sys

# define the grid with the given dimensions and weights
grid = [
    [5, 2, 8, 4, 1],
    [9, 3, 6, 8, 7],
    [1, 1, 1, 1, 1],
    [3, 6, 8, 9, 2],
    [2, 3, 1, 2, 4]
]

# set the start and end nodes
start = (0, 0)
end = (4, 4)

# define the nodes of the graph
class Node:
    def __init__(self, position):
        self.position = position
        self.min_distance = sys.maxsize
        self.visited = False
        self.edges = []

    def add_edge(self, node):
        x2, y2 = node.position
        weight = grid[x2][y2]
        self.edges.append((weight, node))

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

# create the graph from the grid
graph = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            continue
        node = Node((i, j))
        graph[(i, j)] = node

# add edges to the graph
for node in graph.values():
    i, j = node.position
    if i > 0 and grid[i-1][j] != 0:
        node.add_edge(graph[(i-1, j)])
    if i < len(grid)-1 and grid[i+1][j] != 0:
        node.add_edge(graph[(i+1, j)])
    if j > 0 and grid[i][j-1] != 0:
        node.add_edge(graph[(i, j-1)])
    if j < len(grid[i])-1 and grid[i][j+1] != 0:
        node.add_edge(graph[(i, j+1)])

# Dijkstra's algorithm to find the shortest path
start_node = graph[start]
end_node = graph[end]
start_node.min_distance = 0
heap = [(start_node.min_distance, start_node)]

while heap:
    current_distance, current_node = heapq.heappop(heap)
    if current_node.visited:
        continue
    current_node.visited = True
    if current_node == end_node:
        break
    for edge in current_node.edges:
        weight, neighbor = edge
        distance = current_distance + weight
        if distance < neighbor.min_distance:
            neighbor.min_distance = distance
            heapq.heappush(heap, (distance, neighbor))

# print the shortest path
path = []
current_node = end_node
while current_node != start_node:
    path.append(current_node.position)
    current_node = min(current_node.edges, key=lambda x: x[1].min_distance)[1]
path.append(start_node.position)
path.reverse()
print("Shortest path:", path)