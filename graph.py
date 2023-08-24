from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

class SearchAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start_vertex):
        visited = [False] * self.graph.vertices
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.graph.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start_vertex):
        visited = [False] * self.graph.vertices
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.graph.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._dfs_recursive(neighbor, visited)


if __name__ == "__main__":
    num_vertices = 7
    graph = Graph(num_vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)

    search_algo = SearchAlgorithm(graph)
    print("BFS:")
    search_algo.bfs(0)
    print("\nDFS:")
    search_algo.dfs(0)
