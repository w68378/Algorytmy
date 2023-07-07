class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    def dfs(self, start_vertex, visited):
        visited[start_vertex] = True
        print(start_vertex, end=" ")

        for neighbor in self.adj_list[start_vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_vertex):
        visited = [False] * self.num_vertices
        print("Przechodzenie grafu metodą DFS:")
        self.dfs(start_vertex, visited)

def main():
    num_vertices = 6
    graph = Graph(num_vertices)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    start_vertex = 0
    graph.dfs_traversal(start_vertex)


if __name__ == "__main__":
    main()
