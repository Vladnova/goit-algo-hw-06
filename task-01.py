import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Депо", "Вокзальна", "Університет", "Театральна", "Золоті ворота", "Хрещатик"]
G.add_nodes_from(stations)


edges = [
    ("Депо", "Вокзальна"),
    ("Вокзальна", "Університет"),
    ("Університет", "Театральна"),
    ("Театральна", "Золоті ворота"),
    ("Театральна", "Хрещатик"),
    ("Хрещатик", "Депо"),
    ("Депо", "Золоті ворота"),
]


G.add_edges_from(edges)
pos = nx.circular_layout(G)


edge_labels = {
    ("Депо", "Вокзальна"): "1",
    ("Вокзальна", "Університет"): "2",
    ("Університет", "Театральна"): "2",
    ("Театральна", "Золоті ворота"): "5",
    ("Театральна", "Хрещатик"): "3",
    ("Хрещатик", "Депо"): "4",
    ("Депо", "Золоті ворота"): "5",
}


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


nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="green",
    font_size=12,
)

plt.title("Схема руху метрополітену")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)


print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")