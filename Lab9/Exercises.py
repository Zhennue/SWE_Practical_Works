from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}  # Stores weights for weighted graphs

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
        if weight is not None:
            self.weights[(vertex1, vertex2)] = weight
            self.weights[(vertex2, vertex1)] = weight

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    # 1. BFS-based Shortest Path
    def shortest_path_bfs(self, start_vertex, end_vertex):
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])
        visited.add(start_vertex)

        while queue:
            current, path = queue.popleft()
            if current == end_vertex:
                return path
            
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # Return None if no path exists

    # 2. Cycle Detection in Undirected Graph
    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    # 3. Dijkstra's Algorithm for Shortest Path in Weighted Graph
    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.graph[current_vertex]:
                weight = self.weights.get((current_vertex, neighbor), float('inf'))
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    # 4. Check if the Graph is Bipartite
    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                color[vertex] = 0
                queue = deque([vertex])

                while queue:
                    current = queue.popleft()
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

print("\nShortest path from 0 to 3 (BFS):", g.shortest_path_bfs(0, 3))
print("Does the graph have a cycle?", g.has_cycle())

# For Dijkstra's, let's create a weighted graph
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 8)
print("\nDijkstra's shortest paths from 0:", g.dijkstra(0))

print("Is the graph bipartite?", g.is_bipartite())