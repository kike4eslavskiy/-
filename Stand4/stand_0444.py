import timeit
def wave_algorithm(edges, start, end):
    """Реализация волнового алгоритма."""
    vertices = get_vertices(edges)
    num_vertices = count_vertices(edges)
    
 time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')