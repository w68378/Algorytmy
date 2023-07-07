class Graph:
    def __init__(self, num_vertices, directed=False, weighted=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.weighted = weighted
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=None):
        if source < 0 or source >= self.num_vertices or destination < 0 or destination >= self.num_vertices:
            raise ValueError("Nieprawidłowe indeksy wierzchołków.")

        self.adj_matrix[source][destination] = weight if self.weighted else 1
        self.adj_list[source].append((destination, weight))

        if not self.directed:
            self.adj_matrix[destination][source] = weight if self.weighted else 1
            self.adj_list[destination].append((source, weight))

    def print_adj_matrix(self):
        print("Macierz sąsiedztwa:")
        for row in self.adj_matrix:
            print(row)

    def print_adj_list(self):
        print("Lista sąsiedztwa:")
        for vertex, neighbors in enumerate(self.adj_list):
            print(f"{vertex}: {neighbors}")

    def draw_graph(self):
        print("Interpretacja graficzna:")
        for vertex in range(self.num_vertices):
            neighbors = self.adj_list[vertex]
            print(f"{vertex} -> ", end="")
            for neighbor in neighbors:
                destination, weight = neighbor
                if self.weighted:
                    print(f"{destination}({weight}) ", end="")
                else:
                    print(destination, end=" ")
            print()


def build_graph():
    print("Witaj w programie do budowania grafów!")
    graph_type = input("Podaj rodzaj grafu (skierowany, nieskierowany, ważony): ")
    num_vertices = int(input("Podaj liczbę wierzchołków: "))

    directed = False
    weighted = False

    if graph_type.lower() == "skierowany":
        directed = True
    elif graph_type.lower() == "ważony":
        weighted = True

    graph = Graph(num_vertices, directed, weighted)
    num_edges = int(input("Podaj liczbę połączeń: "))

    for _ in range(num_edges):
        source = int(input("Podaj wierzchołek źródłowy: "))
        destination = int(input("Podaj wierzchołek docelowy: "))
        if weighted:
            weight = float(input("Podaj wagę: "))
            graph.add_edge(source, destination, weight)
        else:
            graph.add_edge(source, destination)

    graph.print_adj_matrix()
    graph.print_adj_list()
    graph.draw_graph()


build_graph()