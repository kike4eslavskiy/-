import timeit
def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)
 time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')