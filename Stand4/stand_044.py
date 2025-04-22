import timeit
def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)
 time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')