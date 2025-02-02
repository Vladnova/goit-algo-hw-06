import heapq
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Депо", "Вокзальна", "Університет", "Театральна", "Золоті ворота", "Хрещатик"]
G.add_nodes_from(stations)


edges = [
    ("Депо", "Вокзальна", 1),
    ("Вокзальна", "Університет", 2),
    ("Університет", "Театральна", 2),
    ("Театральна", "Золоті ворота", 5),
    ("Театральна", "Хрещатик", 3),
    ("Хрещатик", "Депо", 4),
    ("Депо", "Золоті ворота", 5),
]

G.add_weighted_edges_from(edges)


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


all_distances = {node: dijkstra(G, node) for node in G.nodes}


print("Найкоротші відстані між усіма парами вершин:")
for source in all_distances:
    for target in all_distances[source]:
        print(f"Від {source} до {target}: відстань {all_distances[source][target]}")


pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="green",
    node_size=3500,
    edge_color="red",
    font_size=8,
    font_color="white",
)


edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Схема метрополітену з вагами ребер")
plt.show()