import heapq
import networkx as nx
import matplotlib.pyplot as plt

def is_valid(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

def generate_moves(x, y):
    moves = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2)
    ]
    return [(a, b) for a, b in moves if is_valid(a, b)]

def dijkstra_shortest_paths(start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current, path) = heapq.heappop(heap)

        if current in visited:
            continue

        path = path + [current]
        if current == end:
            return path

        visited.add(current)

        for move in generate_moves(*current):
            if move not in visited:
                next_cost = cost + 1  # Weight of each move is 1
                heapq.heappush(heap, (next_cost, move, path))

    return None

def create_oriented_graph(path):
    G = nx.DiGraph()

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    return G

def draw_oriented_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=800, node_color='orange', connectionstyle='arc3,rad=0.1')

def save_graph_images(graph, file_name):
    plt.figure(figsize=(8, 8))
    draw_oriented_graph(graph)
    plt.savefig(file_name + '.png', format='png')
    plt.show()

if __name__ == "__main__":
    initial_cell = tuple(map(int, input("Enter initial cell (e.g., 1 1): ").split()))
    final_cell = tuple(map(int, input("Enter final cell (e.g., 8 8): ").split()))

    shortest_path = dijkstra_shortest_paths(initial_cell, final_cell)

    if shortest_path:
        print("Shortest path:")
        print(shortest_path)

        graph = create_oriented_graph(shortest_path)

        # Save graph as a DOT file
        nx.drawing.nx_pydot.write_dot(graph, "./shortest_path.dot")
        print("Oriented graph has been saved as 'shortest_path.dot'")

        # Save graph as a PNG image
        save_graph_images(graph, "./shortest_path")
        print("Oriented graph image has been saved as 'shortest_path.png'")
    else:
        print("No valid path exists.")
