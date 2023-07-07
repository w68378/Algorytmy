import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight):
        self.adj_list[source].append((destination, weight))

    def dijkstra(self, source):
        distance = [float('inf')] * self.num_vertices
        distance[source] = 0

        heap = [(0, source)]
        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distance[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        return distance

def main():
    num_vertices = 6
    graph = Graph(num_vertices)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 4)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 3)
    graph.add_edge(3, 5, 6)
    graph.add_edge(4, 5, 2)

    source = 0
    distances = graph.dijkstra(source)

    print(f"Najkrótsze odległości od wierzchołka {source}:")
    for vertex, distance in enumerate(distances):
        print(f"Wierzchołek {vertex}: {distance}")


if __name__ == "__main__":
    main()
