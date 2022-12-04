def Fib(n):
    F = [0]*(n+1)*2
    F[0] = 0
    F[1] = 1
    for i in range(2,(n*2)+2):
        F[i] = F[i-1]+F[i-2]
    return F[n]

class Router:
    def __init__(self,right):
        self.top = 0
        self.down = 0
        self.left = 0
        self.right = right

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


